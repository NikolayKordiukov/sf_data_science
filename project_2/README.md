# Проект 2. Анализ вакансий из HeadHunter

## Оглавление  
[1. Описание проекта](https://github.com/NikolayKordiukov/sf_data_science/tree/master/project_2/README.md#Описание-проекта)  
[2. Какой кейс решаем?](https://github.com/NikolayKordiukov/sf_data_science/tree/master/project_2/README.md#Какой-кейс-решаем)  
[3. Краткая информация о данных](https://github.com/NikolayKordiukov/sf_data_science/tree/master/project_2/README.md#Краткая-информация-о-данных)  
[4. Этапы работы над проектом](https://github.com/NikolayKordiukov/sf_data_science/tree/master/project_2/README.md#Этапы-работы-над-проектом)  
[5. Результат](https://github.com/NikolayKordiukov/sf_data_science/tree/master/project_2/README.md#Результат)    
[6. Выводы](https://github.com/NikolayKordiukov/sf_data_science/tree/master/project_2/README.md#Выводы) 

### Описание проекта    
Выполнение анализа данных вакансий от HeadHunter путем исследования и преобразования данных.

:arrow_up:[к оглавлению](https://github.com/NikolayKordiukov/sf_data_science/tree/master/project_2/README.md#Оглавление)


### Какой кейс решаем?    
Нужно сделать анализ вакансий, выполнив ряд последовательных этапов и действий в них, а также ответив на вопросы.

**Условия работы:**  
- Предоставляется схема базы данных
- К базе данных делаются запросы
- На каждом этапе проекта задаются вопросы, связанные с результатами, получаемыми на этом этапе в результате выполнения запросов


**Метрика качества**     
Ответить на все ключевые вопросы, подтвердив свои ответы написанным кодом и выводами

**Что практикуем**     
1. Учимся писать хороший код запросов SQL
2. Учимся писать хороший код на python
3. Учимся исследовать и преобразовывать данные
4. Учимся писать выводы


### Краткая информация о данных
Все необходимые таблицы находятся в схеме public базы данных project_sql (оформляется отдельным подключением в самом проекте)
  
:arrow_up:[к оглавлению](https://github.com/NikolayKordiukov/sf_data_science/tree/master/project_2/README.md#Оглавление)


### Этапы работы над проектом  
1. Знакомство с данными.
2. Предварительный анализ данных. Ответы на вопросы, связанные с ними. Написание выводов
3. Детальный анализ вакансий. Ответы на вопросы, связанные с ними. Написание выводов
4. Анализ работодателей. Ответы на вопросы, связанные с ними. Написание выводов
5. Предметный анализ. Ответы на вопросы, связанные с ними. Написание выводов
6. Общие выводы.
7. Дополнительные исследования. Написание выводов.


:arrow_up:[к оглавлению](https://github.com/NikolayKordiukov/sf_data_science/tree/master/project_2/README.md#Оглавление)


### Результаты:  
1. На все вопросы даны ответы.
2. Написаные необходимые выводы о закономерностях либо комментарии к полученным цифрам
3. В блоках кода указаны комментарии по выполняемым операциям

:arrow_up:[к оглавлению](https://github.com/NikolayKordiukov/sf_data_science/tree/master/project_2/README.md#Оглавление)


### Выводы:  
1. Исходный массив данных достаточно большой
2. Детальный анализ показал, что в целом данные соответствуют действительности и могут быть использованы для последующей обработки:
    * Наибольшая для вакансий  -  в крупных городах, столицах и миллиониках
    * Часть данных по заработной плате отсутствует, но оставшейся информации достаточно для дальнейшего исследования
    * Работодатели в основном ищут сотрудников на полную занятость и нечасто готовы предлагать удалённую работу или гибкий график
    * Работодатели стараются искать сотрудников с опытом
3. Аналих работодателй показал, что:
    * Наибольшие доли вакансий формируют крупные компании, которые представлены в различных регионах (Яндекс, Ростелеком, Тинькофф, СБЕР, Газпром нефть)
    * Крупные компании, размещают вакансии в нескольких регионах
    * Более подробные выводы -  в соответствующем блоке проекта
4. Предметный анализа вакансий DS показал:
    * Доля вакансий, имеющих отношение к данным в общем объеме вакансий - мала , а для начинающих DS-специалистов - ещё меньше
    * Навык "Python" в качестве ключевого нужен в большем количестве вакансий, чем навык "SQL" или "postgres" 
    * Для вакансий DS в среднем указывают больше 6 ключевых навыков
    * Более подробные выводы -  в соответствующем блоке проекта


:arrow_up:[к оглавлению](https://github.com/NikolayKordiukov/sf_data_science/tree/master/project_2/README.md#Оглавление)


Если информация по этому проекту покажется вам интересной или полезной, то я буду очень вам благодарен, если отметите репозиторий и профиль ⭐️⭐️⭐️