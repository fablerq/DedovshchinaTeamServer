### Server for 'Дедовщина' Team on 'Цифровой Прорыв' hackathon

Endpoints:

- GET /calc - get normalized address for single string 
- POST /calc/csv - get url for csv file with normalized addresses from source file
- GET /files?data=filename - get calculated csv file by name

GET calc?data=<filename>

![Alt text](imgs/calc.png?raw=true "calc")

POST calc/csv/

![Alt text](imgs/calc-csv.png?raw=true "calc/csv")

GET files/<filename>

![Alt text](imgs/files.png?raw=true "files")
