# Data set format
## Header
- first row has 7 values:
    - number of nodes [N]
    - number of centers [k]
    - number of blue nodes [B]
    = number of red nodes [R]
    - minimum blue coverage [b]
    - minimum red coverage [r]
    - optimal radius [opt] that covers [b] blue points and [r] red points
    - unclustered points for this problem instance [out]
- e.g. "[N] [k] [B] [R] [b] [r] [opt] [out]"

# Subsequent data    
- subsequent N rows have 3 values:
    - x coordinate
    - y coordinate
    - colour class