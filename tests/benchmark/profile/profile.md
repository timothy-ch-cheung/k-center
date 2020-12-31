```
profile_pbs.py
         3957396 function calls (3957394 primitive calls) in 1.349 seconds

   Ordered by: cumulative time

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.002    0.002    1.349    1.349 C:\Users\timch\Documents\projects\k-center\src\kcenter\pbs\pbs.py:440(solve)
      794    0.009    0.000    1.275    0.002 C:\Users\timch\Documents\projects\k-center\src\kcenter\pbs\pbs.py:251(local_search)
     2371    0.092    0.000    1.075    0.000 C:\Users\timch\Documents\projects\k-center\src\kcenter\pbs\pbs.py:200(find_pair)
    12281    0.214    0.000    0.548    0.000 C:\Users\timch\Documents\projects\k-center\src\kcenter\pbs\pbs.py:137(add_center)
   509807    0.177    0.000    0.541    0.000 C:\Users\timch\Documents\projects\k-center\venv\lib\site-packages\networkx\classes\graph.py:441(__getitem__)
    11151    0.077    0.000    0.369    0.000 C:\Users\timch\Documents\projects\k-center\src\kcenter\pbs\pbs.py:180(remove_center)
    92353    0.120    0.000    0.291    0.000 C:\Users\timch\Documents\projects\k-center\src\kcenter\pbs\pbs.py:159(find_next)
      168    0.001    0.000    0.197    0.001 C:\Users\timch\Documents\projects\k-center\src\kcenter\pbs\pbs.py:338(crossover_directed)
      336    0.001    0.000    0.194    0.001 C:\Users\timch\Documents\projects\k-center\src\kcenter\pbs\pbs.py:359(generate_child)
   509807    0.137    0.000    0.186    0.000 C:\Users\timch\Documents\projects\k-center\venv\lib\site-packages\networkx\classes\graph.py:339(adj)
   509807    0.135    0.000    0.178    0.000 C:\Users\timch\Documents\projects\k-center\venv\lib\site-packages\networkx\classes\coreviews.py:78(__getitem__)
     2371    0.004    0.000    0.104    0.000 C:\Users\timch\Documents\projects\k-center\venv\lib\site-packages\networkx\classes\function.py:820(get_edge_attributes)
     2371    0.036    0.000    0.094    0.000 C:\Users\timch\Documents\projects\k-center\venv\lib\site-packages\networkx\classes\function.py:848(<dictcomp>)
  1019614    0.093    0.000    0.093    0.000 C:\Users\timch\Documents\projects\k-center\venv\lib\site-packages\networkx\classes\coreviews.py:41(__init__)
   132776    0.045    0.000    0.057    0.000 C:\Users\timch\Documents\projects\k-center\venv\lib\site-packages\networkx\classes\reportviews.py:772(__iter__)
   509807    0.050    0.000    0.050    0.000 C:\Users\timch\Documents\projects\k-center\venv\lib\site-packages\networkx\classes\coreviews.py:50(__getitem__)
     1184    0.017    0.000    0.044    0.000 C:\Users\timch\Documents\projects\k-center\src\kcenter\pbs\pbs.py:41(init_nearest_centers)
     7850    0.021    0.000    0.030    0.000 {built-in method builtins.max}
   184676    0.028    0.000    0.028    0.000 C:\Users\timch\Documents\projects\k-center\src\kcenter\pbs\pbs.py:15(__init__)
     4295    0.002    0.000    0.019    0.000 C:\Users\timch\Documents\projects\k-center\src\kcenter\pbs\pbs.py:239(get_furthest_point)
      168    0.001    0.000    0.017    0.000 C:\Users\timch\Documents\projects\k-center\src\kcenter\pbs\pbs.py:291(mutation_random)
      168    0.001    0.000    0.014    0.000 C:\Users\timch\Documents\projects\k-center\src\kcenter\pbs\pbs.py:326(crossover_random)
    79114    0.013    0.000    0.013    0.000 {built-in method builtins.min}
   130405    0.011    0.000    0.011    0.000 C:\Users\timch\Documents\projects\k-center\venv\lib\site-packages\networkx\classes\reportviews.py:701(<lambda>)
      504    0.002    0.000    0.010    0.000 C:\Users\timch\Documents\projects\k-center\src\kcenter\pbs\pbs.py:306(mutation_directed)
      672    0.006    0.000    0.009    0.000 C:\Users\timch\Documents\projects\k-center\src\kcenter\pbs\pbs.py:399(update_population)
    42950    0.008    0.000    0.008    0.000 C:\Users\timch\Documents\projects\k-center\src\kcenter\pbs\pbs.py:246(<lambda>)
      536    0.002    0.000    0.008    0.000 C:\Users\timch\AppData\Local\Programs\Python\Python39\lib\random.py:374(sample)
     3845    0.002    0.000    0.006    0.000 C:\Users\timch\AppData\Local\Programs\Python\Python39\lib\random.py:343(choice)
     7682    0.004    0.000    0.005    0.000 C:\Users\timch\Documents\projects\k-center\venv\lib\site-packages\networkx\classes\graph.py:656(nodes)
     2997    0.003    0.000    0.005    0.000 C:\Users\timch\Documents\projects\k-center\src\kcenter\pbs\pbs.py:126(get_nwk)
     4749    0.003    0.000    0.005    0.000 C:\Users\timch\AppData\Local\Programs\Python\Python39\lib\random.py:237(_randbelow_with_getrandbits)
     2371    0.002    0.000    0.003    0.000 C:\Users\timch\Documents\projects\k-center\venv\lib\site-packages\networkx\classes\reportviews.py:1019(__call__)
     2371    0.001    0.000    0.003    0.000 C:\Users\timch\Documents\projects\k-center\venv\lib\site-packages\networkx\classes\graph.py:1242(edges)
     2997    0.002    0.000    0.003    0.000 C:\Users\timch\Documents\projects\k-center\src\kcenter\pbs\pbs.py:114(linear_search)
      536    0.003    0.000    0.003    0.000 {built-in method _warnings.warn}
     1072    0.001    0.000    0.002    0.000 {built-in method builtins.isinstance}
    26081    0.002    0.000    0.002    0.000 {method 'items' of 'dict' objects}
    23321    0.002    0.000    0.002    0.000 {built-in method builtins.len}
    11840    0.002    0.000    0.002    0.000 C:\Users\timch\Documents\projects\k-center\src\kcenter\pbs\pbs.py:72(<lambda>)
     2371    0.001    0.000    0.002    0.000 C:\Users\timch\Documents\projects\k-center\venv\lib\site-packages\networkx\classes\reportviews.py:992(__init__)
    13882    0.002    0.000    0.002    0.000 {method 'add' of 'set' objects}
     1072    0.000    0.000    0.002    0.000 C:\Users\timch\AppData\Local\Programs\Python\Python39\lib\abc.py:96(__instancecheck__)
     2371    0.002    0.000    0.002    0.000 C:\Users\timch\Documents\projects\k-center\venv\lib\site-packages\networkx\classes\reportviews.py:687(__init__)
     1072    0.001    0.000    0.001    0.000 {built-in method _abc._abc_instancecheck}
     7682    0.001    0.000    0.001    0.000 C:\Users\timch\Documents\projects\k-center\venv\lib\site-packages\networkx\classes\reportviews.py:176(__init__)
    11151    0.001    0.000    0.001    0.000 {method 'remove' of 'set' objects}
     4161    0.001    0.000    0.001    0.000 {method 'intersection' of 'set' objects}
     3376    0.001    0.000    0.001    0.000 C:\Users\timch\Documents\projects\k-center\venv\lib\site-packages\networkx\classes\reportviews.py:180(__len__)
     9039    0.001    0.000    0.001    0.000 {method 'getrandbits' of '_random.Random' objects}
     7682    0.001    0.000    0.001    0.000 C:\Users\timch\Documents\projects\k-center\venv\lib\site-packages\networkx\classes\reportviews.py:198(__call__)
     5994    0.001    0.000    0.001    0.000 C:\Users\timch\Documents\projects\k-center\venv\lib\site-packages\networkx\classes\reportviews.py:186(__getitem__)
  538/537    0.000    0.000    0.001    0.000 C:\Users\timch\AppData\Local\Programs\Python\Python39\lib\abc.py:100(__subclasscheck__)
     3889    0.001    0.000    0.001    0.000 C:\Users\timch\Documents\projects\k-center\src\kcenter\pbs\pbs.py:414(is_between)
      794    0.001    0.000    0.001    0.000 C:\Users\timch\Documents\projects\k-center\src\kcenter\pbs\pbs.py:79(copy)
     1688    0.000    0.000    0.001    0.000 C:\Users\timch\Documents\projects\k-center\venv\lib\site-packages\networkx\classes\reportviews.py:183(__iter__)
     1680    0.001    0.000    0.001    0.000 {method 'difference' of 'set' objects}
  538/537    0.000    0.000    0.001    0.000 {built-in method _abc._abc_subclasscheck}
     4749    0.001    0.000    0.001    0.000 {method 'bit_length' of 'int' objects}
     1978    0.001    0.000    0.001    0.000 C:\Users\timch\Documents\projects\k-center\src\kcenter\pbs\pbs.py:36(__init__)
      168    0.000    0.000    0.001    0.000 C:\Users\timch\AppData\Local\Programs\Python\Python39\lib\random.py:334(randint)
     1588    0.000    0.000    0.000    0.000 C:\Users\timch\Documents\projects\k-center\venv\lib\site-packages\networkx\classes\graph.py:754(number_of_nodes)
     2371    0.000    0.000    0.000    0.000 {built-in method builtins.hasattr}
      168    0.000    0.000    0.000    0.000 C:\Users\timch\AppData\Local\Programs\Python\Python39\lib\random.py:290(randrange)
     2371    0.000    0.000    0.000    0.000 C:\Users\timch\Documents\projects\k-center\venv\lib\site-packages\networkx\classes\graph.py:1439(is_multigraph)
     1688    0.000    0.000    0.000    0.000 {built-in method builtins.iter}
      168    0.000    0.000    0.000    0.000 C:\Users\timch\AppData\Local\Programs\Python\Python39\lib\typing.py:256(inner)
      794    0.000    0.000    0.000    0.000 {built-in method math.floor}
     2371    0.000    0.000    0.000    0.000 {method 'values' of 'dict' objects}
      168    0.000    0.000    0.000    0.000 C:\Users\timch\AppData\Local\Programs\Python\Python39\lib\random.py:503(uniform)
      536    0.000    0.000    0.000    0.000 C:\Users\timch\AppData\Local\Programs\Python\Python39\lib\_collections_abc.py:311(__subclasshook__)
      168    0.000    0.000    0.000    0.000 {method 'union' of 'set' objects}
      744    0.000    0.000    0.000    0.000 C:\Users\timch\Documents\projects\k-center\src\kcenter\pbs\pbs.py:432(<lambda>)
      168    0.000    0.000    0.000    0.000 {method 'random' of '_random.Random' objects}
        8    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
        2    0.000    0.000    0.000    0.000 C:\Users\timch\AppData\Local\Programs\Python\Python39\lib\_collections_abc.py:405(__subclasshook__)
        8    0.000    0.000    0.000    0.000 C:\Users\timch\Documents\projects\k-center\src\kcenter\pbs\pbs.py:468(<lambda>)
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
```