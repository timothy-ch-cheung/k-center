# Rows = time measured for algorithm to run, Columns(A,B,C) = algorithm
# Algorithms A and B are from the same distribution, while C is from a different distribution

y <- matrix(c( 5,  4,  1,
               2,  3,  4,
              16, 15, 1,
               5,  6,  7,
              10,  9,  1,
              19, 18, 1,
              10,  9,  6),
            nrow = 7, byrow = TRUE,
            dimnames =
            list(Problem = c("pmed01","pmed02","pmed03","pmed04","pmed05","pmed06","pmed07"),
                 Algorithm = LETTERS[1:3]))
y
(qTst <- quade.test(y))

library(PMCMRplus)
quadeAllPairsTest(y, dist="TDist", p.adjust.method="holm")