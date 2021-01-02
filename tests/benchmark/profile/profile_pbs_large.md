```
395535725 function calls (395535723 primitive calls) in 159.834 seconds

   Ordered by: cumulative time

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.006    0.006  159.834  159.834 C:\Users\timch\Documents\projects\k-center\src\kcenter\pbs\pbs.py:451(solve)
      680    0.124    0.000  155.560    0.229 C:\Users\timch\Documents\projects\k-center\src\kcenter\pbs\pbs.py:269(local_search)
    28588   22.175    0.001  151.936    0.005 C:\Users\timch\Documents\projects\k-center\src\kcenter\pbs\pbs.py:201(find_pair)
   387808   14.263    0.000   84.355    0.000 C:\Users\timch\Documents\projects\k-center\src\kcenter\pbs\pbs.py:182(remove_center)
 13994612   39.895    0.000   69.991    0.000 C:\Users\timch\Documents\projects\k-center\src\kcenter\pbs\pbs.py:159(find_next)
   389301   28.233    0.000   36.563    0.000 C:\Users\timch\Documents\projects\k-center\src\kcenter\pbs\pbs.py:138(add_center)
216440713   22.348    0.000   22.348    0.000 C:\Users\timch\Documents\projects\k-center\venv\lib\site-packages\networkx\classes\coreviews.py:50(__getitem__)
 17150155    6.140    0.000   19.002    0.000 C:\Users\timch\Documents\projects\k-center\venv\lib\site-packages\networkx\classes\graph.py:441(__getitem__)
 17150155    4.767    0.000    6.566    0.000 C:\Users\timch\Documents\projects\k-center\venv\lib\site-packages\networkx\classes\graph.py:339(adj)
 17150155    4.774    0.000    6.296    0.000 C:\Users\timch\Documents\projects\k-center\venv\lib\site-packages\networkx\classes\coreviews.py:78(__getitem__)
 43512206    6.220    0.000    6.220    0.000 {built-in method builtins.min}
     1184    1.251    0.001    4.190    0.004 C:\Users\timch\Documents\projects\k-center\src\kcenter\pbs\pbs.py:41(init_nearest_centers)
 28701435    4.087    0.000    4.087    0.000 C:\Users\timch\Documents\projects\k-center\src\kcenter\pbs\pbs.py:15(__init__)
 34300310    3.321    0.000    3.321    0.000 C:\Users\timch\Documents\projects\k-center\venv\lib\site-packages\networkx\classes\coreviews.py:41(__init__)
      504    0.016    0.000    1.540    0.003 C:\Users\timch\Documents\projects\k-center\src\kcenter\pbs\pbs.py:318(mutation_directed)
    38067    0.689    0.000    1.515    0.000 {built-in method builtins.max}
    36883    0.041    0.000    1.498    0.000 C:\Users\timch\Documents\projects\k-center\src\kcenter\pbs\pbs.py:245(get_furthest_point)
      168    0.005    0.000    1.260    0.008 C:\Users\timch\Documents\projects\k-center\src\kcenter\pbs\pbs.py:351(crossover_directed)
      336    0.002    0.000    1.251    0.004 C:\Users\timch\Documents\projects\k-center\src\kcenter\pbs\pbs.py:372(generate_child)
  4241545    0.794    0.000    0.794    0.000 C:\Users\timch\Documents\projects\k-center\src\kcenter\pbs\pbs.py:252(<lambda>)
      168    0.002    0.000    0.729    0.004 C:\Users\timch\Documents\projects\k-center\src\kcenter\pbs\pbs.py:339(crossover_random)
      168    0.002    0.000    0.726    0.004 C:\Users\timch\Documents\projects\k-center\src\kcenter\pbs\pbs.py:303(mutation_random)
      680    0.008    0.000    0.227    0.000 C:\Users\timch\Documents\projects\k-center\src\kcenter\pbs\pbs.py:257(initilise_local_search)
    30425    0.052    0.000    0.135    0.000 C:\Users\timch\AppData\Local\Programs\Python\Python39\lib\random.py:343(choice)
    61345    0.071    0.000    0.100    0.000 C:\Users\timch\Documents\projects\k-center\venv\lib\site-packages\networkx\classes\graph.py:656(nodes)
   530254    0.096    0.000    0.096    0.000 {method 'add' of 'set' objects}
    30080    0.084    0.000    0.092    0.000 C:\Users\timch\Documents\projects\k-center\src\kcenter\pbs\pbs.py:115(linear_search)
    35076    0.049    0.000    0.073    0.000 C:\Users\timch\AppData\Local\Programs\Python\Python39\lib\random.py:237(_randbelow_with_getrandbits)
    30080    0.049    0.000    0.073    0.000 C:\Users\timch\Documents\projects\k-center\src\kcenter\pbs\pbs.py:127(get_nwk)
   387808    0.051    0.000    0.051    0.000 {method 'remove' of 'set' objects}
   387808    0.049    0.000    0.049    0.000 {method 'items' of 'dict' objects}
   136160    0.032    0.000    0.032    0.000 C:\Users\timch\Documents\projects\k-center\src\kcenter\pbs\pbs.py:72(<lambda>)
    61345    0.029    0.000    0.029    0.000 C:\Users\timch\Documents\projects\k-center\venv\lib\site-packages\networkx\classes\reportviews.py:176(__init__)
    70087    0.022    0.000    0.022    0.000 {built-in method builtins.len}
      616    0.006    0.000    0.022    0.000 C:\Users\timch\AppData\Local\Programs\Python\Python39\lib\random.py:374(sample)
    60160    0.017    0.000    0.017    0.000 C:\Users\timch\Documents\projects\k-center\venv\lib\site-packages\networkx\classes\reportviews.py:186(__getitem__)
    66384    0.013    0.000    0.013    0.000 {method 'getrandbits' of '_random.Random' objects}
    61345    0.011    0.000    0.011    0.000 C:\Users\timch\Documents\projects\k-center\venv\lib\site-packages\networkx\classes\reportviews.py:198(__call__)
    35076    0.011    0.000    0.011    0.000 {method 'bit_length' of 'int' objects}
      672    0.006    0.000    0.008    0.000 C:\Users\timch\Documents\projects\k-center\src\kcenter\pbs\pbs.py:410(update_population)
      616    0.007    0.000    0.007    0.000 {built-in method _warnings.warn}
     1232    0.001    0.000    0.005    0.000 {built-in method builtins.isinstance}
     1232    0.000    0.000    0.004    0.000 C:\Users\timch\AppData\Local\Programs\Python\Python39\lib\abc.py:96(__instancecheck__)
     1232    0.002    0.000    0.004    0.000 {built-in method _abc._abc_instancecheck}
     5290    0.003    0.000    0.003    0.000 {method 'difference' of 'set' objects}
     1363    0.002    0.000    0.002    0.000 {method 'intersection' of 'set' objects}
  618/617    0.000    0.000    0.002    0.000 C:\Users\timch\AppData\Local\Programs\Python\Python39\lib\abc.py:100(__subclasscheck__)
  618/617    0.001    0.000    0.001    0.000 {built-in method _abc._abc_subclasscheck}
     2370    0.001    0.000    0.001    0.000 C:\Users\timch\Documents\projects\k-center\venv\lib\site-packages\networkx\classes\reportviews.py:180(__len__)
     1185    0.001    0.000    0.001    0.000 C:\Users\timch\Documents\projects\k-center\venv\lib\site-packages\networkx\classes\reportviews.py:183(__iter__)
      680    0.001    0.000    0.001    0.000 C:\Users\timch\Documents\projects\k-center\src\kcenter\pbs\pbs.py:79(copy)
      421    0.001    0.000    0.001    0.000 {built-in method math.log}
     1864    0.001    0.000    0.001    0.000 C:\Users\timch\Documents\projects\k-center\src\kcenter\pbs\pbs.py:36(__init__)
     1360    0.000    0.000    0.001    0.000 C:\Users\timch\Documents\projects\k-center\venv\lib\site-packages\networkx\classes\graph.py:754(number_of_nodes)
      680    0.001    0.000    0.001    0.000 {built-in method math.floor}
      168    0.000    0.000    0.001    0.000 C:\Users\timch\AppData\Local\Programs\Python\Python39\lib\random.py:334(randint)
     1185    0.001    0.000    0.001    0.000 {built-in method builtins.iter}
      168    0.000    0.000    0.000    0.000 {method 'union' of 'set' objects}
      168    0.000    0.000    0.000    0.000 C:\Users\timch\AppData\Local\Programs\Python\Python39\lib\random.py:290(randrange)
      421    0.000    0.000    0.000    0.000 {built-in method math.ceil}
      168    0.000    0.000    0.000    0.000 C:\Users\timch\AppData\Local\Programs\Python\Python39\lib\typing.py:256(inner)
      616    0.000    0.000    0.000    0.000 C:\Users\timch\AppData\Local\Programs\Python\Python39\lib\_collections_abc.py:311(__subclasshook__)
     1164    0.000    0.000    0.000    0.000 C:\Users\timch\Documents\projects\k-center\src\kcenter\pbs\pbs.py:425(is_between)
      168    0.000    0.000    0.000    0.000 C:\Users\timch\AppData\Local\Programs\Python\Python39\lib\random.py:503(uniform)
      168    0.000    0.000    0.000    0.000 {method 'random' of '_random.Random' objects}
        8    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
        8    0.000    0.000    0.000    0.000 C:\Users\timch\Documents\projects\k-center\src\kcenter\pbs\pbs.py:481(<lambda>)
        8    0.000    0.000    0.000    0.000 C:\Users\timch\Documents\projects\k-center\src\kcenter\pbs\pbs.py:443(<lambda>)
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
        2    0.000    0.000    0.000    0.000 C:\Users\timch\AppData\Local\Programs\Python\Python39\lib\_collections_abc.py:405(__subclasshook__)


         395535725 function calls (395535723 primitive calls) in 159.834 seconds

   Ordered by: internal time

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
 13994612   39.895    0.000   69.991    0.000 C:\Users\timch\Documents\projects\k-center\src\kcenter\pbs\pbs.py:159(find_next)
   389301   28.233    0.000   36.563    0.000 C:\Users\timch\Documents\projects\k-center\src\kcenter\pbs\pbs.py:138(add_center)
216440713   22.348    0.000   22.348    0.000 C:\Users\timch\Documents\projects\k-center\venv\lib\site-packages\networkx\classes\coreviews.py:50(__getitem__)
    28588   22.175    0.001  151.936    0.005 C:\Users\timch\Documents\projects\k-center\src\kcenter\pbs\pbs.py:201(find_pair)
   387808   14.263    0.000   84.355    0.000 C:\Users\timch\Documents\projects\k-center\src\kcenter\pbs\pbs.py:182(remove_center)
 43512206    6.220    0.000    6.220    0.000 {built-in method builtins.min}
 17150155    6.140    0.000   19.002    0.000 C:\Users\timch\Documents\projects\k-center\venv\lib\site-packages\networkx\classes\graph.py:441(__getitem__)
 17150155    4.774    0.000    6.296    0.000 C:\Users\timch\Documents\projects\k-center\venv\lib\site-packages\networkx\classes\coreviews.py:78(__getitem__)
 17150155    4.767    0.000    6.566    0.000 C:\Users\timch\Documents\projects\k-center\venv\lib\site-packages\networkx\classes\graph.py:339(adj)
 28701435    4.087    0.000    4.087    0.000 C:\Users\timch\Documents\projects\k-center\src\kcenter\pbs\pbs.py:15(__init__)
 34300310    3.321    0.000    3.321    0.000 C:\Users\timch\Documents\projects\k-center\venv\lib\site-packages\networkx\classes\coreviews.py:41(__init__)
     1184    1.251    0.001    4.190    0.004 C:\Users\timch\Documents\projects\k-center\src\kcenter\pbs\pbs.py:41(init_nearest_centers)
  4241545    0.794    0.000    0.794    0.000 C:\Users\timch\Documents\projects\k-center\src\kcenter\pbs\pbs.py:252(<lambda>)
    38067    0.689    0.000    1.515    0.000 {built-in method builtins.max}
      680    0.124    0.000  155.560    0.229 C:\Users\timch\Documents\projects\k-center\src\kcenter\pbs\pbs.py:269(local_search)
   530254    0.096    0.000    0.096    0.000 {method 'add' of 'set' objects}
    30080    0.084    0.000    0.092    0.000 C:\Users\timch\Documents\projects\k-center\src\kcenter\pbs\pbs.py:115(linear_search)
    61345    0.071    0.000    0.100    0.000 C:\Users\timch\Documents\projects\k-center\venv\lib\site-packages\networkx\classes\graph.py:656(nodes)
    30425    0.052    0.000    0.135    0.000 C:\Users\timch\AppData\Local\Programs\Python\Python39\lib\random.py:343(choice)
   387808    0.051    0.000    0.051    0.000 {method 'remove' of 'set' objects}
    35076    0.049    0.000    0.073    0.000 C:\Users\timch\AppData\Local\Programs\Python\Python39\lib\random.py:237(_randbelow_with_getrandbits)
   387808    0.049    0.000    0.049    0.000 {method 'items' of 'dict' objects}
    30080    0.049    0.000    0.073    0.000 C:\Users\timch\Documents\projects\k-center\src\kcenter\pbs\pbs.py:127(get_nwk)
    36883    0.041    0.000    1.498    0.000 C:\Users\timch\Documents\projects\k-center\src\kcenter\pbs\pbs.py:245(get_furthest_point)
   136160    0.032    0.000    0.032    0.000 C:\Users\timch\Documents\projects\k-center\src\kcenter\pbs\pbs.py:72(<lambda>)
    61345    0.029    0.000    0.029    0.000 C:\Users\timch\Documents\projects\k-center\venv\lib\site-packages\networkx\classes\reportviews.py:176(__init__)
    70087    0.022    0.000    0.022    0.000 {built-in method builtins.len}
    60160    0.017    0.000    0.017    0.000 C:\Users\timch\Documents\projects\k-center\venv\lib\site-packages\networkx\classes\reportviews.py:186(__getitem__)
      504    0.016    0.000    1.540    0.003 C:\Users\timch\Documents\projects\k-center\src\kcenter\pbs\pbs.py:318(mutation_directed)
    66384    0.013    0.000    0.013    0.000 {method 'getrandbits' of '_random.Random' objects}
    61345    0.011    0.000    0.011    0.000 C:\Users\timch\Documents\projects\k-center\venv\lib\site-packages\networkx\classes\reportviews.py:198(__call__)
    35076    0.011    0.000    0.011    0.000 {method 'bit_length' of 'int' objects}
      680    0.008    0.000    0.227    0.000 C:\Users\timch\Documents\projects\k-center\src\kcenter\pbs\pbs.py:257(initilise_local_search)
      616    0.007    0.000    0.007    0.000 {built-in method _warnings.warn}
        1    0.006    0.006  159.834  159.834 C:\Users\timch\Documents\projects\k-center\src\kcenter\pbs\pbs.py:451(solve)
      616    0.006    0.000    0.022    0.000 C:\Users\timch\AppData\Local\Programs\Python\Python39\lib\random.py:374(sample)
      672    0.006    0.000    0.008    0.000 C:\Users\timch\Documents\projects\k-center\src\kcenter\pbs\pbs.py:410(update_population)
      168    0.005    0.000    1.260    0.008 C:\Users\timch\Documents\projects\k-center\src\kcenter\pbs\pbs.py:351(crossover_directed)
     5290    0.003    0.000    0.003    0.000 {method 'difference' of 'set' objects}
     1232    0.002    0.000    0.004    0.000 {built-in method _abc._abc_instancecheck}
      336    0.002    0.000    1.251    0.004 C:\Users\timch\Documents\projects\k-center\src\kcenter\pbs\pbs.py:372(generate_child)
      168    0.002    0.000    0.726    0.004 C:\Users\timch\Documents\projects\k-center\src\kcenter\pbs\pbs.py:303(mutation_random)
     1363    0.002    0.000    0.002    0.000 {method 'intersection' of 'set' objects}
      168    0.002    0.000    0.729    0.004 C:\Users\timch\Documents\projects\k-center\src\kcenter\pbs\pbs.py:339(crossover_random)
     1232    0.001    0.000    0.005    0.000 {built-in method builtins.isinstance}
  618/617    0.001    0.000    0.001    0.000 {built-in method _abc._abc_subclasscheck}
      421    0.001    0.000    0.001    0.000 {built-in method math.log}
     2370    0.001    0.000    0.001    0.000 C:\Users\timch\Documents\projects\k-center\venv\lib\site-packages\networkx\classes\reportviews.py:180(__len__)
      680    0.001    0.000    0.001    0.000 C:\Users\timch\Documents\projects\k-center\src\kcenter\pbs\pbs.py:79(copy)
     1185    0.001    0.000    0.001    0.000 C:\Users\timch\Documents\projects\k-center\venv\lib\site-packages\networkx\classes\reportviews.py:183(__iter__)
     1864    0.001    0.000    0.001    0.000 C:\Users\timch\Documents\projects\k-center\src\kcenter\pbs\pbs.py:36(__init__)
      680    0.001    0.000    0.001    0.000 {built-in method math.floor}
     1185    0.001    0.000    0.001    0.000 {built-in method builtins.iter}
     1232    0.000    0.000    0.004    0.000 C:\Users\timch\AppData\Local\Programs\Python\Python39\lib\abc.py:96(__instancecheck__)
      168    0.000    0.000    0.000    0.000 {method 'union' of 'set' objects}
     1360    0.000    0.000    0.001    0.000 C:\Users\timch\Documents\projects\k-center\venv\lib\site-packages\networkx\classes\graph.py:754(number_of_nodes)
      421    0.000    0.000    0.000    0.000 {built-in method math.ceil}
      168    0.000    0.000    0.000    0.000 C:\Users\timch\AppData\Local\Programs\Python\Python39\lib\typing.py:256(inner)
      616    0.000    0.000    0.000    0.000 C:\Users\timch\AppData\Local\Programs\Python\Python39\lib\_collections_abc.py:311(__subclasshook__)
     1164    0.000    0.000    0.000    0.000 C:\Users\timch\Documents\projects\k-center\src\kcenter\pbs\pbs.py:425(is_between)
      168    0.000    0.000    0.000    0.000 C:\Users\timch\AppData\Local\Programs\Python\Python39\lib\random.py:290(randrange)
  618/617    0.000    0.000    0.002    0.000 C:\Users\timch\AppData\Local\Programs\Python\Python39\lib\abc.py:100(__subclasscheck__)
      168    0.000    0.000    0.000    0.000 C:\Users\timch\AppData\Local\Programs\Python\Python39\lib\random.py:503(uniform)
      168    0.000    0.000    0.001    0.000 C:\Users\timch\AppData\Local\Programs\Python\Python39\lib\random.py:334(randint)
      168    0.000    0.000    0.000    0.000 {method 'random' of '_random.Random' objects}
        8    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
        8    0.000    0.000    0.000    0.000 C:\Users\timch\Documents\projects\k-center\src\kcenter\pbs\pbs.py:481(<lambda>)
        8    0.000    0.000    0.000    0.000 C:\Users\timch\Documents\projects\k-center\src\kcenter\pbs\pbs.py:443(<lambda>)
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
        2    0.000    0.000    0.000    0.000 C:\Users\timch\AppData\Local\Programs\Python\Python39\lib\_collections_abc.py:405(__subclasshook__)


cost 12.214213621159692
```