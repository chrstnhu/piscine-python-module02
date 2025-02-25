from TinyStatistician import TinyStatistician

tstat = TinyStatistician()
a = [1, 42, 300, 10, 59]
print(f"a: {a}\n")

result = tstat.mean(a)
print(f"Mean : {result}")
# Expected result: 82.4

result = tstat.median(a)
print(f"Median : {result}")
# Expected result: 42.0

result = tstat.quartile(a)
print(f"Quartile : {result}")
# Expected result: [10.0, 59.0]

result = tstat.var(a)
print(f"Variance : {result}")
# Expected result: 12279.439999999999

result = tstat.std(a)
print(f"Standard deviation : {result}")
# Expected result: 110.81263465868862