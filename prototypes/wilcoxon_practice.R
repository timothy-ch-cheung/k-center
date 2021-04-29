# Data in two numeric vectors Wilcoxon
# ++++++++++++++++++++++++++
# Weight of the mice before treatment
before <-c(200.1, 190.9, 192.7, 213, 241.4, 196.9, 172.2, 185.5, 205.2, 193.7)
# Weight of the mice after treatment
after <-c(392.9, 393.2, 345.1, 393, 434, 427.9, 422, 383.9, 392.3, 352.2)
# Create a data frame
my_data <- data.frame(
                group = rep(c("before", "after"), each = 10),
                weight = c(before,  after)
                )

print(my_data)

res <- wilcox.test(before, after, paired = TRUE)

res$p.value