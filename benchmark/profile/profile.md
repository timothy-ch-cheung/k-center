```
15520199 function calls (15520197 primitive calls) in 4.897 seconds

   Ordered by: cumulative time

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.003    0.003    4.897    4.897 C:\Users\timch\Documents\projects\k-center\src\kcenter\pbs\pbs.py:441(solve)
      834    0.013    0.000    4.533    0.005 C:\Users\timch\Documents\projects\k-center\src\kcenter\pbs\pbs.py:262(local_search)
     4962    0.275    0.000    3.561    0.001 C:\Users\timch\Documents\projects\k-center\src\kcenter\pbs\pbs.py:199(find_pair)
  2019950    0.681    0.000    2.095    0.000 C:\Users\timch\Documents\projects\k-center\venv\lib\site-packages\networkx\classes\graph.py:441(__getitem__)
    19989    0.623    0.000    1.631    0.000 C:\Users\timch\Documents\projects\k-center\src\kcenter\pbs\pbs.py:136(add_center)
    18641    0.204    0.000    1.423    0.000 C:\Users\timch\Documents\projects\k-center\src\kcenter\pbs\pbs.py:179(remove_center)
   125684    0.386    0.000    1.217    0.000 C:\Users\timch\Documents\projects\k-center\src\kcenter\pbs\pbs.py:158(find_next)
      168    0.003    0.000    0.900    0.005 C:\Users\timch\Documents\projects\k-center\src\kcenter\pbs\pbs.py:339(crossover_directed)
      336    0.001    0.000    0.894    0.003 C:\Users\timch\Documents\projects\k-center\src\kcenter\pbs\pbs.py:360(generate_child)
  2019950    0.520    0.000    0.717    0.000 C:\Users\timch\Documents\projects\k-center\venv\lib\site-packages\networkx\classes\graph.py:339(adj)
     4962    0.010    0.000    0.702    0.000 C:\Users\timch\Documents\projects\k-center\venv\lib\site-packages\networkx\classes\function.py:820(get_edge_attributes)
  2019950    0.529    0.000    0.697    0.000 C:\Users\timch\Documents\projects\k-center\venv\lib\site-packages\networkx\classes\coreviews.py:78(__getitem__)
     4962    0.276    0.000    0.674    0.000 C:\Users\timch\Documents\projects\k-center\venv\lib\site-packages\networkx\classes\function.py:848(<dictcomp>)
  1046982    0.315    0.000    0.398    0.000 C:\Users\timch\Documents\projects\k-center\venv\lib\site-packages\networkx\classes\reportviews.py:772(__iter__)
  4039900    0.364    0.000    0.364    0.000 C:\Users\timch\Documents\projects\k-center\venv\lib\site-packages\networkx\classes\coreviews.py:41(__init__)
     1184    0.100    0.000    0.309    0.000 C:\Users\timch\Documents\projects\k-center\src\kcenter\pbs\pbs.py:40(init_nearest_centers)
  2019950    0.197    0.000    0.197    0.000 C:\Users\timch\Documents\projects\k-center\venv\lib\site-packages\networkx\classes\coreviews.py:50(__getitem__)
      834    0.005    0.000    0.139    0.000 C:\Users\timch\Documents\projects\k-center\src\kcenter\pbs\pbs.py:250(initilise_local_search)
      504    0.007    0.000    0.120    0.000 C:\Users\timch\Documents\projects\k-center\src\kcenter\pbs\pbs.py:307(mutation_directed)
    13290    0.078    0.000    0.112    0.000 {built-in method builtins.max}
  1042020    0.075    0.000    0.075    0.000 C:\Users\timch\Documents\projects\k-center\venv\lib\site-packages\networkx\classes\reportviews.py:701(<lambda>)
      168    0.001    0.000    0.067    0.000 C:\Users\timch\Documents\projects\k-center\src\kcenter\pbs\pbs.py:292(mutation_random)
     7144    0.003    0.000    0.065    0.000 C:\Users\timch\Documents\projects\k-center\src\kcenter\pbs\pbs.py:238(get_furthest_point)
      168    0.001    0.000    0.064    0.000 C:\Users\timch\Documents\projects\k-center\src\kcenter\pbs\pbs.py:327(crossover_random)
   342122    0.052    0.000    0.052    0.000 C:\Users\timch\Documents\projects\k-center\src\kcenter\pbs\pbs.py:14(__init__)
   259915    0.041    0.000    0.041    0.000 {built-in method builtins.min}
   142880    0.029    0.000    0.029    0.000 C:\Users\timch\Documents\projects\k-center\src\kcenter\pbs\pbs.py:245(<lambda>)
      589    0.003    0.000    0.014    0.000 C:\Users\timch\AppData\Local\Programs\Python\Python39\lib\random.py:374(sample)
     6654    0.004    0.000    0.013    0.000 C:\Users\timch\AppData\Local\Programs\Python\Python39\lib\random.py:343(choice)
    13804    0.008    0.000    0.011    0.000 C:\Users\timch\Documents\projects\k-center\venv\lib\site-packages\networkx\classes\graph.py:656(nodes)
     6310    0.006    0.000    0.011    0.000 C:\Users\timch\Documents\projects\k-center\src\kcenter\pbs\pbs.py:125(get_nwk)
     4962    0.004    0.000    0.010    0.000 C:\Users\timch\Documents\projects\k-center\venv\lib\site-packages\networkx\classes\reportviews.py:1019(__call__)
     8927    0.006    0.000    0.009    0.000 C:\Users\timch\AppData\Local\Programs\Python\Python39\lib\random.py:237(_randbelow_with_getrandbits)
   104202    0.008    0.000    0.008    0.000 {method 'items' of 'dict' objects}
     4962    0.003    0.000    0.007    0.000 C:\Users\timch\Documents\projects\k-center\venv\lib\site-packages\networkx\classes\graph.py:1242(edges)
     6310    0.006    0.000    0.007    0.000 C:\Users\timch\Documents\projects\k-center\src\kcenter\pbs\pbs.py:113(linear_search)
      672    0.005    0.000    0.007    0.000 C:\Users\timch\Documents\projects\k-center\src\kcenter\pbs\pbs.py:400(update_population)
     4962    0.005    0.000    0.005    0.000 C:\Users\timch\Documents\projects\k-center\venv\lib\site-packages\networkx\classes\reportviews.py:687(__init__)
      589    0.005    0.000    0.005    0.000 {built-in method _warnings.warn}
    23680    0.005    0.000    0.005    0.000 C:\Users\timch\Documents\projects\k-center\src\kcenter\pbs\pbs.py:71(<lambda>)
     4962    0.004    0.000    0.005    0.000 C:\Users\timch\Documents\projects\k-center\venv\lib\site-packages\networkx\classes\reportviews.py:992(__init__)
     1178    0.001    0.000    0.004    0.000 {built-in method builtins.isinstance}
    25168    0.004    0.000    0.004    0.000 {method 'add' of 'set' objects}
     1178    0.000    0.000    0.003    0.000 C:\Users\timch\AppData\Local\Programs\Python\Python39\lib\abc.py:96(__instancecheck__)
    13804    0.003    0.000    0.003    0.000 C:\Users\timch\Documents\projects\k-center\venv\lib\site-packages\networkx\classes\reportviews.py:176(__init__)
    24085    0.003    0.000    0.003    0.000 {built-in method builtins.len}
     1178    0.001    0.000    0.003    0.000 {built-in method _abc._abc_instancecheck}
    18641    0.002    0.000    0.002    0.000 {method 'remove' of 'set' objects}
    12620    0.002    0.000    0.002    0.000 C:\Users\timch\Documents\projects\k-center\venv\lib\site-packages\networkx\classes\reportviews.py:186(__getitem__)
    16097    0.002    0.000    0.002    0.000 {method 'getrandbits' of '_random.Random' objects}
     3192    0.002    0.000    0.002    0.000 {method 'difference' of 'set' objects}
    13804    0.002    0.000    0.002    0.000 C:\Users\timch\Documents\projects\k-center\venv\lib\site-packages\networkx\classes\reportviews.py:198(__call__)
  591/590    0.000    0.000    0.001    0.000 C:\Users\timch\AppData\Local\Programs\Python\Python39\lib\abc.py:100(__subclasscheck__)
     1857    0.001    0.000    0.001    0.000 {method 'intersection' of 'set' objects}
     4962    0.001    0.000    0.001    0.000 {built-in method builtins.hasattr}
  591/590    0.001    0.000    0.001    0.000 {built-in method _abc._abc_subclasscheck}
     8927    0.001    0.000    0.001    0.000 {method 'bit_length' of 'int' objects}
     2368    0.001    0.000    0.001    0.000 C:\Users\timch\Documents\projects\k-center\venv\lib\site-packages\networkx\classes\reportviews.py:180(__len__)
     1184    0.000    0.000    0.001    0.000 C:\Users\timch\Documents\projects\k-center\venv\lib\site-packages\networkx\classes\reportviews.py:183(__iter__)
      834    0.001    0.000    0.001    0.000 C:\Users\timch\Documents\projects\k-center\src\kcenter\pbs\pbs.py:78(copy)
     4962    0.001    0.000    0.001    0.000 C:\Users\timch\Documents\projects\k-center\venv\lib\site-packages\networkx\classes\graph.py:1439(is_multigraph)
     2018    0.001    0.000    0.001    0.000 C:\Users\timch\Documents\projects\k-center\src\kcenter\pbs\pbs.py:35(__init__)
     1668    0.000    0.000    0.001    0.000 C:\Users\timch\Documents\projects\k-center\venv\lib\site-packages\networkx\classes\graph.py:754(number_of_nodes)
     4962    0.001    0.000    0.001    0.000 {method 'values' of 'dict' objects}
      168    0.000    0.000    0.001    0.000 C:\Users\timch\AppData\Local\Programs\Python\Python39\lib\random.py:334(randint)
      834    0.000    0.000    0.000    0.000 {built-in method math.floor}
      168    0.000    0.000    0.000    0.000 C:\Users\timch\AppData\Local\Programs\Python\Python39\lib\typing.py:256(inner)
      168    0.000    0.000    0.000    0.000 C:\Users\timch\AppData\Local\Programs\Python\Python39\lib\random.py:290(randrange)
     1184    0.000    0.000    0.000    0.000 {built-in method builtins.iter}
     1557    0.000    0.000    0.000    0.000 C:\Users\timch\Documents\projects\k-center\src\kcenter\pbs\pbs.py:415(is_between)
      589    0.000    0.000    0.000    0.000 C:\Users\timch\AppData\Local\Programs\Python\Python39\lib\_collections_abc.py:311(__subclasshook__)
      168    0.000    0.000    0.000    0.000 {method 'union' of 'set' objects}
      168    0.000    0.000    0.000    0.000 C:\Users\timch\AppData\Local\Programs\Python\Python39\lib\random.py:503(uniform)
      168    0.000    0.000    0.000    0.000 {method 'random' of '_random.Random' objects}
      104    0.000    0.000    0.000    0.000 C:\Users\timch\Documents\projects\k-center\src\kcenter\pbs\pbs.py:433(<lambda>)
        8    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
        8    0.000    0.000    0.000    0.000 C:\Users\timch\Documents\projects\k-center\src\kcenter\pbs\pbs.py:471(<lambda>)
        2    0.000    0.000    0.000    0.000 C:\Users\timch\AppData\Local\Programs\Python\Python39\lib\_collections_abc.py:405(__subclasshook__)
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
        

cost 5.00000000000001
```