# -*- coding: utf-8 -*-
"""
@file
@brief Datasets from :epkg:`Eurostat`.
"""
import os
import gzip
import numpy
import pandas
import pyensae.datasource
from pyquickhelper.loghelper import noLOG


def table_mortalite_euro_stat(
        url="http://ec.europa.eu/eurostat/estat-navtree-portlet-prod/BulkDownloadListing?file=data/",
        name="demo_mlifetable.tsv.gz", final_name="mortalite.txt",
        whereTo=".", stop_at=None, fLOG=noLOG):
    """
    This function retrieves mortality table from `EuroStat
    <http://ec.europa.eu/eurostat/fr>`_ through
    `table de mortalité <http://www.data-publica.com/
    opendata/7098--population-et-conditions-sociales-table-de-mortalite-de-1960-a-2010>`_
    (*this link is currently broken, data-publica does not provide
    such a database anymore, a copy is provided*).

    @param      url         data source
    @param      name        data table name
    @param      final_name  the data is compressed, it needs to be uncompressed into a file,
                            this parameter defines its name
    @param      whereTo     data needs to be downloaded, location of this place
    @param      stop_at     the overall process is quite long, if not None,
                            it only keeps the first rows
    @param      fLOG        logging function
    @return                 data_frame

    The function checks the file final_name exists.
    If it is the case, the data is not downloaded twice.
    The header contains a weird format as coordinates are separated by a comma::

        indic_de,sex,age,geo\\time	2013 	2012 	2011 	2010 	2009

    We need to preprocess the data to split this information into columns.
    The overall process takes 4-5 minutes, 10 seconds to download (< 10 Mb),
    4-5 minutes to preprocess the data (it could be improved). The processed data
    contains the following columns::

        ['annee', 'valeur', 'age', 'age_num', 'indicateur', 'genre', 'pays']

    Columns *age* and *age_num* look alike. *age_num* is numeric and is equal
    to *age* except when *age_num* is 85. Everybody above that age
    fall into the same category. The table contains many indicators:

    * PROBSURV: Probabilité de survie entre deux âges exacts (px)
    * LIFEXP: Esperance de vie à l'âge exact (ex)
    * SURVIVORS: Nombre des survivants à l'âge exact (lx)
    * PYLIVED: Nombre d'années personnes vécues entre deux âges exacts (Lx)
    * DEATHRATE: Taux de mortalité à l'âge x (Mx)
    * PROBDEATH: Probabilité de décès entre deux âges exacts (qx)
    * TOTPYLIVED: Nombre total d'années personne vécues après l'âge exact (Tx)
    """
    if os.path.exists(final_name) and os.stat(final_name).st_size > 1e7:
        return final_name

    temp = final_name + ".remove.txt"
    if not os.path.exists(temp) or os.stat(temp).st_size < 1e7:
        local = pyensae.datasource.download_data(
            name, url=url, whereTo=whereTo)
        local = local[0] + ".gz"
        with gzip.open(local, 'rb') as f:
            file_content = f.read()
        content = str(file_content, encoding="utf8")
        with open(temp, "w", encoding="utf8") as f:
            f.write(content)

    def format_age(s):
        "local function"
        if s.startswith("Y_"):
            if s.startswith("Y_LT"):
                return "YLT" + s[4:]
            if s.startswith("Y_GE"):
                return "YGE" + s[4:]
            raise SyntaxError(s)  # pragma: no cover
        i = int(s.strip("Y"))
        return "Y%02d" % i

    def format_age_num(s):
        "local function"
        if s.startswith("Y_"):
            if s.startswith("Y_LT"):
                return float(s.replace("Y_LT", ""))
            if s.startswith("Y_GE"):
                return float(s.replace("Y_GE", ""))
            raise SyntaxError(s)  # pragma: no cover
        i = int(s.strip("Y"))
        return float(i)

    def format_value(s):
        "local function"
        if s.strip() == ":":
            return numpy.nan
        return float(s.strip(" ebp"))

    fLOG("step 0, reading")
    dff = pandas.read_csv(temp, sep="\t", encoding="utf8")

    if stop_at is not None:
        fLOG("step 0, shortening")
        dfsmall = dff.head(n=stop_at)
        df = dfsmall
    else:
        df = dff

    fLOG("step 1, size=", df.shape)
    dfi = df.reset_index().set_index("indic_de,sex,age,geo\\time")
    dfi = dfi.drop('index', axis=1)
    dfs = dfi.stack()
    dfs = pandas.DataFrame({"valeur": dfs})

    fLOG("step 2, size=", dfs.shape)
    dfs["valeur"] = dfs["valeur"].astype(str)
    dfs["valeur"] = dfs["valeur"].apply(format_value)
    dfs = dfs[dfs.valeur >= 0].copy()
    dfs = dfs.reset_index()
    dfs.columns = ["index", "annee", "valeur"]

    fLOG("step 3, size=", dfs.shape)
    dfs["age"] = dfs["index"].apply(lambda i: format_age(i.split(",")[2]))
    dfs["age_num"] = dfs["index"].apply(
        lambda i: format_age_num(i.split(",")[2]))
    dfs["indicateur"] = dfs["index"].apply(lambda i: i.split(",")[0])
    dfs["genre"] = dfs["index"].apply(lambda i: i.split(",")[1])
    dfs["pays"] = dfs["index"].apply(lambda i: i.split(",")[3])

    fLOG("step 4")
    dfy = dfs.drop('index', axis=1)
    dfy.to_csv(final_name, sep="\t", encoding="utf8", index=False)
    return final_name
