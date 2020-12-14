```
  Ordered by: cumulative time

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.005    0.005    2.567    2.567 src\kcenter\pbs\pbs.py:393(solve)
      826    0.028    0.000    2.422    0.003 src\kcenter\pbs\pbs.py:251(local_search)
     1923    0.206    0.000    2.023    0.001 src\kcenter\pbs\pbs.py:200(find_pair)
    10535    0.437    0.000    1.005    0.000 src\kcenter\pbs\pbs.py:137(add_center)
   437819    0.333    0.000    0.932    0.000 Python\Python36\lib\site-packages\networkx\classes\graph.py:441(__getitem__)
     9373    0.154    0.000    0.686    0.000 src\kcenter\pbs\pbs.py:180(remove_center)
    78784    0.235    0.000    0.530    0.000 src\kcenter\pbs\pbs.py:159(find_next)
      168    0.004    0.000    0.476    0.003 src\kcenter\pbs\pbs.py:329(crossover_directed)
      336    0.002    0.000    0.468    0.001 src\kcenter\pbs\pbs.py:350(generate_child)
   437819    0.240    0.000    0.312    0.000 Python\Python36\lib\site-packages\networkx\classes\graph.py:339(adj)
   437819    0.230    0.000    0.287    0.000 Python\Python36\lib\site-packages\networkx\classes\coreviews.py:78(__getitem__)
     1923    0.010    0.000    0.203    0.000 Python\Python36\lib\site-packages\networkx\classes\function.py:820(get_edge_attributes)
     1923    0.063    0.000    0.144    0.000 Python\Python36\lib\site-packages\networkx\classes\function.py:848(<dictcomp>)
   875638    0.129    0.000    0.129    0.000 Python\Python36\lib\site-packages\networkx\classes\coreviews.py:41(__init__)
     1184    0.042    0.000    0.096    0.000 src\kcenter\pbs\pbs.py:41(init_nearest_centers)
   107688    0.065    0.000    0.081    0.000 Python\Python36\lib\site-packages\networkx\classes\reportviews.py:772(__iter__)
   437819    0.079    0.000    0.079    0.000 Python\Python36\lib\site-packages\networkx\classes\coreviews.py:50(__getitem__)
     7018    0.046    0.000    0.065    0.000 {built-in method builtins.max}
     3911    0.004    0.000    0.046    0.000 src\kcenter\pbs\pbs.py:239(get_furthest_point)
   162018    0.046    0.000    0.046    0.000 src\kcenter\pbs\pbs.py:15(__init__)
     1923    0.028    0.000    0.039    0.000 Python\Python36\lib\site-packages\networkx\classes\graph.py:1242(edges)
      168    0.002    0.000    0.036    0.000 src\kcenter\pbs\pbs.py:284(mutation_random)
      168    0.005    0.000    0.034    0.000 src\kcenter\pbs\pbs.py:317(crossover_random)
    67051    0.030    0.000    0.030    0.000 {built-in method builtins.min}
      504    0.006    0.000    0.023    0.000 src\kcenter\pbs\pbs.py:299(mutation_directed)
     3429    0.006    0.000    0.018    0.000 Python\Python36\lib\random.py:253(choice)
    39110    0.016    0.000    0.016    0.000 src\kcenter\pbs\pbs.py:246(<lambda>)
     6850    0.011    0.000    0.015    0.000 Python\Python36\lib\site-packages\networkx\classes\graph.py:656(nodes)
     4303    0.009    0.000    0.014    0.000 Python\Python36\lib\random.py:223(_randbelow)
   105765    0.013    0.000    0.013    0.000 Python\Python36\lib\site-packages\networkx\classes\reportviews.py:701(<lambda>)
      521    0.005    0.000    0.012    0.000 Python\Python36\lib\random.py:283(sample)
     1923    0.005    0.000    0.011    0.000 Python\Python36\lib\site-packages\networkx\classes\reportviews.py:992(__init__)
     2581    0.007    0.000    0.010    0.000 src\kcenter\pbs\pbs.py:126(get_nwk)
     1923    0.005    0.000    0.009    0.000 Python\Python36\lib\site-packages\networkx\classes\reportviews.py:1019(__call__)
     2581    0.008    0.000    0.009    0.000 src\kcenter\pbs\pbs.py:114(linear_search)
     1923    0.006    0.000    0.006    0.000 {built-in method builtins.hasattr}
     1042    0.002    0.000    0.006    0.000 {built-in method builtins.isinstance}
     1923    0.005    0.000    0.005    0.000 Python\Python36\lib\site-packages\networkx\classes\reportviews.py:687(__init__)
     6850    0.004    0.000    0.004    0.000 Python\Python36\lib\site-packages\networkx\classes\reportviews.py:176(__init__)
     1042    0.002    0.000    0.004    0.000 Python\Python36\lib\abc.py:180(__instancecheck__)
    12090    0.004    0.000    0.004    0.000 {method 'add' of 'set' objects}
     7811    0.003    0.000    0.003    0.000 {method 'getrandbits' of '_random.Random' objects}
    11840    0.003    0.000    0.003    0.000 src\kcenter\pbs\pbs.py:72(<lambda>)
      826    0.003    0.000    0.003    0.000 src\kcenter\pbs\pbs.py:79(copy)
    21153    0.003    0.000    0.003    0.000 {method 'items' of 'dict' objects}
    12514    0.003    0.000    0.003    0.000 {built-in method builtins.len}
     9376    0.003    0.000    0.003    0.000 {method 'remove' of 'set' objects}
     1050    0.002    0.000    0.002    0.000 Python\Python36\lib\_weakrefset.py:70(__contains__)
      168    0.000    0.000    0.002    0.000 Python\Python36\lib\random.py:217(randint)
     1688    0.001    0.000    0.002    0.000 Python\Python36\lib\site-packages\networkx\classes\reportviews.py:183(__iter__)
     1680    0.002    0.000    0.002    0.000 {method 'difference' of 'set' objects}
      168    0.000    0.000    0.002    0.000 Python\Python36\lib\random.py:173(randrange)
     5162    0.001    0.000    0.001    0.000 Python\Python36\lib\site-packages\networkx\classes\reportviews.py:186(__getitem__)
     6850    0.001    0.000    0.001    0.000 Python\Python36\lib\site-packages\networkx\classes\reportviews.py:198(__call__)
     1688    0.001    0.000    0.001    0.000 Python\Python36\lib\site-packages\networkx\classes\reportviews.py:180(__len__)
      168    0.001    0.000    0.001    0.000 Python\Python36\lib\typing.py:676(inner)
     2010    0.001    0.000    0.001    0.000 src\kcenter\pbs\pbs.py:36(__init__)
     4303    0.001    0.000    0.001    0.000 {method 'bit_length' of 'int' objects}
     1652    0.001    0.000    0.001    0.000 Python\Python36\lib\site-packages\networkx\classes\graph.py:754(number_of_nodes)
     1688    0.001    0.000    0.001    0.000 {built-in method builtins.iter}
      680    0.001    0.000    0.001    0.000 {method 'append' of 'list' objects}
     1923    0.000    0.000    0.000    0.000 Python\Python36\lib\site-packages\networkx\classes\graph.py:1439(is_multigraph)
     1923    0.000    0.000    0.000    0.000 {method 'values' of 'dict' objects}
        3    0.000    0.000    0.000    0.000 {built-in method builtins.sorted}
      168    0.000    0.000    0.000    0.000 Python\Python36\lib\random.py:367(uniform)
      168    0.000    0.000    0.000    0.000 {method 'union' of 'set' objects}
      168    0.000    0.000    0.000    0.000 Python\Python36\lib\typing.py:1096(__hash__)
      696    0.000    0.000    0.000    0.000 src\kcenter\pbs\pbs.py:418(<lambda>)
      168    0.000    0.000    0.000    0.000 {method 'random' of '_random.Random' objects}
      3/2    0.000    0.000    0.000    0.000 Python\Python36\lib\abc.py:196(__subclasscheck__)
        7    0.000    0.000    0.000    0.000 Python\Python36\lib\_weakrefset.py:58(__iter__)
      5/4    0.000    0.000    0.000    0.000 {built-in method builtins.issubclass}
        3    0.000    0.000    0.000    0.000 Python\Python36\lib\_weakrefset.py:26(__exit__)
        3    0.000    0.000    0.000    0.000 Python\Python36\lib\_weakrefset.py:81(add)
        3    0.000    0.000    0.000    0.000 Python\Python36\lib\_weakrefset.py:20(__enter__)
        1    0.000    0.000    0.000    0.000 {method '__subclasses__' of 'type' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
        3    0.000    0.000    0.000    0.000 Python\Python36\lib\_weakrefset.py:52(_commit_removals)
        3    0.000    0.000    0.000    0.000 Python\Python36\lib\_weakrefset.py:16(__init__)
        8    0.000    0.000    0.000    0.000 src\kcenter\pbs\pbs.py:422(<lambda>)
        3    0.000    0.000    0.000    0.000 {built-in method builtins.getattr}
        2    0.000    0.000    0.000    0.000 Python\Python36\lib\_collections_abc.py:392(__subclasshook__)
        1    0.000    0.000    0.000    0.000 Python\Python36\lib\_collections_abc.py:302(__subclasshook__)
Process finished with exit code 0

```