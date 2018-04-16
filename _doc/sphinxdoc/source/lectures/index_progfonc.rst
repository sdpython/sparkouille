
===========================
Programmation fonctionnelle
===========================

La programmation fonctionnelle est une bonne introduction
à ce qui est algorithme de streaming simplement parce qu'un
programme en langage fonctionnelle est beaucoup plus simple
à paralléliser en :epkg:`map/reduce` qu'un programme écrit
dans un langage et une syntaxe impérative.

Introductions aux mappers et aux reducers
=========================================

Même s'il n'est pas utilisé pour implémenter
des framework map/reduce car beaucoup trop lent
et surtout très difficile à parlléliser,
le langage :epkg:`python` permet néanmoins de
découvrir les concepts de bases d'un tel système.
Ce module implémenté des fonctions non parallélisées,
:ref:`l-api-mapper-reducer` pour illustrer les concepts
de mapperrs, reducers, combiners.

.. toctree::
    :maxdepth: 1

    ../notebooks/recursive_reducers

Algorithmes
===========

Quelques jeux autour de la programmation
fonctionnelle et des algorithmes implémentés
en :epkg:`Python`. Le langage ne propose
que très peu de fonctionnalités capables de paralléliser
un traitement. Les exemples suivants restent plutôt
théoriques que pratiques à moins de passer à d'autres
langages.

.. toctree::
    :maxdepth: 1

    ../notebooks/reservoir_sampling
    ../notebooks/skewed_dataset
    ../notebooks/skewed_dataset_correction
