
Vieux notebooks sur PIG
-----------------------

:epkg:`PIG` est le premier langage :epkg:`map/reduce`
inventé chez :epkg:`Yahoo` tout comme :epkg:`Hadoop`.
Ce n'est pas le plus élégant et pas le plus intuitif.
S'il est apparemment possible de faire fonctioner 
`PIG sur Spark <https://cwiki.apache.org/confluence/display/PIG/Pig+on+Spark>`_,
le langage ne permet pas d'utiliser les dataframes
qui sont plus rapides. La syntaxe n'est pas la plus facile
lorsqu'il s'agit d'associer un langage fonctionnel
et un langage impératif pour les fonctions qui tournent
qui chaque noeud du cluster. Cette imbrication est mieux faite
avec le langage :epkg:`U-SQL` qui associe :epkg:`SQL` et :epkg:`C#`.
Ces notebooks n'ont pas été mis à jour depuis 2016.