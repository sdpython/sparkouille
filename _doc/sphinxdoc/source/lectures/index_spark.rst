
Introduction à Spark
====================

.. toctree::
    :maxdepth: 1

    spark_install
    ../notebooks/spark_first_steps
    ../notebooks/spark_matrix_3_columns
    ../notebooks/spark_mllib

*Articles*

* `Resilient Distributed Datasets: A Fault-Tolerant Abstraction for In-Memory Cluster Computing <http://www.cs.berkeley.edu/~matei/papers/2012/nsdi_spark.pdf>`_,
  Matei Zaharia, Mosharaf Chowdhury, Tathagata Das, Ankur Dave, Justin Ma, Murphy McCauley, Michael J. Franklin, Scott Shenker, Ion Stoica
* `From scikit-learn to Spark ML <http://blog.xebia.fr/2015/10/08/from-scikit-learn-to-spark-ml/>`_
* `Deep Dive into Catalyst <https://spark-summit.org/2016/events/deep-dive-into-catalyst-apache-spark-20s-optimizer/>`_,
  `Catalyst — Tree Manipulation Framework <https://jaceklaskowski.gitbooks.io/mastering-apache-spark/content/spark-sql-catalyst.html>`_
* `What is Tungsten for Apache Spark? <https://community.hortonworks.com/articles/72502/what-is-tungsten-for-apache-spark.html>`_,
  `Project Tungsten: Bringing Apache Spark Closer to Bare Metal <https://databricks.com/blog/2015/04/28/project-tungsten-bringing-spark-closer-to-bare-metal.html>`_
* `Spark SQL: Another 16x times faster after Tungsten <https://spark-summit.org/east-2017/events/spark-sql-another-16x-faster-after-tungsten/>`_
* `Databricks <https://docs.databricks.com/index.html#>`_

*Articles un peu plus éloignés*

* `Stochastic Gradient Descent Tricks <http://research.microsoft.com/pubs/192769/tricks-2012.pdf>`_, Léon Bottou
* `A Fast Distributed Stochastic Gradient Descent Algorithm for Matrix Factorization <http://jmlr.org/proceedings/papers/v36/li14.pdf>`_, Fanglin Li, Bin Wu, Liutong Xu, Chuan Shi, Jing Shi
* `Parallelized Stochastic Gradient Descent <http://martin.zinkevich.org/publications/nips2010.pdf>`_, Martin A. Zinkevich, Markus Weimer, Alex Smola, Lihong Li
* `Topic Similarity Networks: Visual Analytics for Large Document Sets <http://arxiv.org/pdf/1409.7591v1.pdf>`_, Arun S. Maiya, Robert M. Rolfe
* `Low-dimensional Embeddings for Interpretable Anchor-based Topic Inference <http://mimno.infosci.cornell.edu/papers/EMNLP2014138.pdf>`_, Moontae Lee, David Mimno
* `K-means on Azure <http://apiacoa.org/publications/2010/durutrossi2010k-means-on.pdf>`_, Matthieu Durut, Fabrice Rossi
* `Confidence intervals for AB-test <http://arxiv.org/abs/1501.07768>`_, Cyrille Dubarry
* `Tutorial: Spark-GPU Cluster Dev in a Notebook <https://iamtrask.github.io/2014/11/22/spark-gpu/>`_

*FAQ*

* `Avoid GroupByKey <https://databricks.gitbooks.io/databricks-spark-knowledge-base/content/best_practices/prefer_reducebykey_over_groupbykey.html>`_
* `What is the difference between cache and persist? <https://stackoverflow.com/questions/26870537/what-is-the-difference-between-cache-and-persist>`_

*Modules*

* `spark-sklearn <https://databricks.com/blog/2016/02/08/auto-scaling-scikit-learn-with-apache-spark.html>`_ :
  implémentation d'un grid search distribué pour `scikit-learn <http://scikit-learn.org/>`_.
* `turicreate <https://github.com/apple/turicreate>`_ : mélange de deep learning
  et de *spark*

*Autres librairies / outils*

* `Hadoop <http://hadoop.apache.org/>`_ : système de fichier distribué + Map Reduce simple
* `Kafka <http://kafka.apache.org/>`_ : distributed streaming platform, conçu pour stocker et récupérer en temps réel des événements de sites web
* `Mesos <http://mesos.apache.org/>`_ : Apache Mesos abstracts CPU, memory, storage, and other compute resources away from machines (physical or virtual), `Elixi <https://github.com/ceteri/exelixi/wiki>`_
* `MLlib <https://spark.apache.org/mllib/>`_ : distributed machine learning for Spark
* `Parquet <http://parquet.apache.org/>`_ : Apache Parquet is a columnar storage format available to any project in the Hadoop ecosystem.
* `Presto <https://prestodb.io/>`_ : Distributed SQL Query Engine for Big Data (Facebook)
* `Spark <https://spark.apache.org/>`_ :  Map Reduce, minimise les accès disques, (`DPark <https://github.com/douban/dpark>`_ clone Python de Spark)
* `Spark SQL <https://spark.apache.org/sql/>`_ : SQL distribué, sur couche de Spark
* `Storm <https://storm.apache.org/>`_ : Apache Storm is a free and open source distributed realtime computation system, conçu pour distribuer des pipelines de traitements de données
* `YARN <https://hadoop.apache.org/docs/r2.7.1/hadoop-yarn/hadoop-yarn-site/YARN.html>`_ : Ressource negociator
