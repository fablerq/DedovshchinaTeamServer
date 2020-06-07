### Server for 'Дедовщина' Team on 'Цифровой Прорыв' hackathon

Endpoints:

- GET /calc?data=<linewithtext> - get normalized address for single string 
- POST /calc/csv - get url for csv file with normalized addresses from source file
- GET /files/<filename> - get calculated csv file by name

GET calc?data=<linewithtext>

![Alt text](imgs/calc.png?raw=true "calc")

##### Имплементировано в пакете, но следующие два метода пока не используют пакетные методы, а содана временная функциональность в виде зарузки/отдачи файлов

POST calc/csv/

![Alt text](imgs/calc-csv.png?raw=true "calc/csv")

GET files/<filename>

![Alt text](imgs/files.png?raw=true "files")
