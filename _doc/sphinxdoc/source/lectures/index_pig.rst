
Introduction à PIG
==================

Ces notebooks ont servi de supports à un cours
données à l':epkg:`ENSAE` entre 2015 et 2016.
:epkg:`Spark` a pris le relais depuis.
Les distributions :epkg:`Cloudera` et :epkg:`HortonWork` (Azure)
étaient disponibles à l'époque.

Premier pas avec Cloudera et Azure
++++++++++++++++++++++++++++++++++

Les quatre premiers notebooks montrent les différences
entre les deux distributions pour les opérations les plus
simples comme télécharger, uploader un fichier sur ou depuis
cluster. C'était l'occasion également de tenter de tout faire
depuis un notebook et non pas depuis plusieurs outils,
ligne de commandes, ou scripts. Cette automatisation
est implémenté par le module :epkg:`pyenbc` qui
n'est plus vraiment maintenu. Il reste cependant quelques
fonctionnalités pratique pour se connecter à une machine
distance.

.. toctree::
    :maxdepth: 1

    ../notebooks/pig_cloudera
    ../notebooks/pig_cloudera_correction
    ../notebooks/pig_azure
    ../notebooks/pig_azure_correction

Streaming et paramètres
+++++++++++++++++++++++

Streaming au sens de PIG, c'est à dire la possibilité
de programmer une sorte de *mapper* ou de *reducer*
en :epkg:`Python` plutôt qu'en PIG.
Les paramètres sont une fonctionnalité pour exécuter le même
job PIG avec certaines parties dépendant de variables
qui changent à chaque exécution.

.. toctree::
    :maxdepth: 1

    ../notebooks/pig_streaming
    ../notebooks/pig_streaming_azure_correction
    ../notebooks/pig_streaming_cloudera_correction
    ../notebooks/pig_params_cloudera
    ../notebooks/pig_params_cloudera_correction
    ../notebooks/pig_params_azure
    ../notebooks/pig_params_azure_correction

Algorithmes
+++++++++++

Le hasard est doublement compliqué en environnement
distribuée et sur des grandes données. Le
`réservoir sampling <https://en.wikipedia.org/wiki/Reservoir_sampling>`_
est un exemple de ce qu'on peut faire
(voir aussi :ref:`reservoirsamplingrst`).

.. toctree::
    :maxdepth: 1

    ../notebooks/pig_reservoir_sampling_azure_correction
