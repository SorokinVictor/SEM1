# Задание 1.
# Продакт на главной mail.ru решил протестировать в рекомендательной ленте контента вместо карточек со статьями видеоплеер с короткими видео.
# Нынешний таймспент на юзера в день в среднем равен 25 минут, а стандартная ошибка (SD) равна 156.
# Мы предполагаем, что в новой версии таймспент на юзера в день изменится на 10%.
# Средний трафик 20000 человек в день. Посчитайте сколько дней необходимо держать эксперимент при alpha = 5% и beta = 20% .

import numpy as np
from scipy.stats import norm, t

n = 20000  # среднее количество юзеров в день
sd = 156  # стандартная ошибка
alpha = 0.05  # уровень значимости
beta = 0.2  # вероятность ошибки второго рода
prop_diff = 0.1  # относительное изменение таймспента

se = sd / np.sqrt(n)  # стандартная ошибка среднего
m = se * norm.ppf(1 - alpha/2)  # граница для доверительного интервала
delta = prop_diff * n  # абсолютное изменение таймспента

z_alpha = norm.ppf(1 - alpha)  
z_beta = norm.ppf(1 - beta) 

n_1 = (z_alpha*m + z_beta*sd/delta)**2
n_2 = (z_alpha*m - z_beta*sd/delta)**2
n_round = np.ceil(max(n_1, n_2))
days = np.ceil(n_round/n)  # количество дней

print(f"Необходимо собрать данные в течении {int(days)} дней")

# Ответ: Необходимо собрать данные в течении 1 дней

# Задача 2.

# Наша продуктовая команда в ecommerce магазине планирует запустить тест, направленный на ускорение загрузки сайта.
# Одна из основных метрик bounce rate в GA = 40%. 
# Мы предполагаем, что при оптимизации сайта она изменится минимум на 20%. 
# Средний трафик 4000 человек в день. 
# Посчитайте сколько нам нужно дней держать эксперимент при alpha = 5% и beta = 20%

# импорт необходимых библиотек
from statsmodels.stats.power import tt_ind_solve_power, zt_ind_solve_power
from statsmodels.stats.proportion import proportion_effectsize
from statsmodels.stats.meta_analysis import effectsize_smd
from typing import Union
import plotly.graph_objects as go
from scipy import stats
from math import asin
import numpy as np

def calc_proportion_es(prob1: float, prob2: float):
    
    return abs(proportion_effectsize(prob1, prob2))

def calc_proportion_es_alt(conv1: float, conv2:float, prob1:float, prob2: float):
    
    return 2  * asin(np.sqrt(conv1/nobs1)) - 2 * asin(np.sqrt(conv2/nobs2))

def calc_continuous_es(mean_control: Union[float, int],
                       std_control: Union[float, int],
                       mean_test: Union[float, int],
                       std_test: Union[float, int]):
    
    return abs(effectsize_smd(mean_control,
                              std_control,
                              1e4,
                              mean_test,
                              std_test,
                              1e4)[0])

def calc_continuous_es_alt(mean_control: Union[float, int],
                           std_control: Union[float, int],
                           mean_test: Union[float, int],
                           std_test: Union[float, int]):
    
    effect_size = (mean_test - mean_control) / ((std_control**2 + std_test**2) / 2) ** 0.5
    return effect_size
    
def calc_sample_size_continuous(effect_size: float,
                     alpha: float = .05,
                     beta: float = .2,
                     ratio: Union[float, int] = 1):
    
    n = tt_ind_solve_power(effect_size=effect_size,
                           alpha=alpha,
                           power=(1 - beta),
                           ratio=ratio,
                  )
    return int(n * 2)

def calc_sample_size_proportion(effect_size: float,
                     alpha: float = .05,
                     beta: float = .2,
                     ratio: Union[float, int] = 1):
    
    n = zt_ind_solve_power(effect_size=effect_size,
                           alpha=alpha,
                           power=(1 - beta),
                           ratio=ratio,
                  )
    return int(n * 2)

BR_1, BR_2 = 0.40, 0.32

es_prop = calc_proportion_es(BR_1, BR_2)
es_prop

calc_sample_size_proportion(es_prop)

DAU = 4000

res = 1126 / DAU
print(res)

# Ответ: длительность теста должна быть 0.28 дня