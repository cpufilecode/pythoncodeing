"""

>>> people={100:'yang',200:'jang',300:'o'}
>>> list(people. keys())
[100, 200, 300]
>>> list(people. values())
['yang', 'jang', 'o']
>>> list(people. items())
[(100, 'yang'), (200, 'jang'), (300, 'o')]
>>> people. get(200)
'jang'
>>> del(people[100])
>>> people
{200: 'jang', 300: 'o'}

"""