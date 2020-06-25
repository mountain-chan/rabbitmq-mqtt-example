a="""import timeit

long1 = timeit.timeit('ex1()',
                      setup='from mqtt.client_publish import ex1',
                      number=1)

print(long1)

long = timeit.timeit('ex2()',
                     setup='from mqtt.client_publish import ex2',
                     number=1)

print(long)
"""

"""hhhhh"""

