'''
idade = input('qual sua idade:')
qual sua idade:>? 980
idade >= 18
Traceback (most recent call last):
  File "/usr/lib/python3.6/site-packages/IPython/core/interactiveshell.py", line 2881, in run_code
    exec(code_obj, self.user_global_ns, self.user_ns)
  File "<ipython-input-75-267bf5e3502d>", line 1, in <module>
    idade >= 18
TypeError: '>=' not supported between instances of 'str' and 'int'


o error ocorre pois a função input armazena o dado
como uma strig e não podemos comparar string com int

Correção:

idade = int(input('qual sua idade:'))
qual sua idade:>? 980
idade >= 18
Out[78]: True

no input eu coloquei a função int() isso vai dizer ao python
para não armazenar o dados como strigs e sim como int == inteiros

'''