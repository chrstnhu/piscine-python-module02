from TinyStatistician import TinyStatistician

tstat = TinyStatistician()
a = [1, 42, 300, 10, 59]
print(f"a: {a}\n")

result = tstat.mean(a)
print(f"Mean : {result}")
# # Expected result: 82.4

result = tstat.median(a)
print(f"Median : {result}")
# Expected result: 42.0


# tstat.quartile(a)
# # Expected result: [10.0, 59.0]
# tstat.var(a)
# # Expected result: 12279.439999999999
# tstat.std(a)
# # Expected result: 110.81263465868862