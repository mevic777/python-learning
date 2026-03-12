--S? se g?seasc? angaja?ii ce au func?ii a c?ror cantitate de caractere nu este mai mare decât suma angaja?ilor din  Briceni.
USE ANGAJAT

--S? se afi?eze num?rul de angaja?i ?i salariul mediu pentru fiecare ?ar?. Aranja?i informa?ia în ordine alfabetic dup? denumirea ??rii.
SELECT AVG(SALARIU) AS SAL,COUNT(*) AS NR,LOCALITATE
	FROM ANGAJARE A INNER JOIN ANGAJAT AA ON A.ANGAJAT_ID=AA.ANGAJAT_ID
	INNER JOIN LOC_STR LS ON LS.LOC_STR_ID=AA.LOC_STR_ID
	INNER JOIN LOCALITATE L ON L.LOCALITATE_ID=LS.LOCALITATE_ID
	GROUP BY LOCALITATE
	ORDER BY LOCALITATE ASC

--S? se afi?eze to?i angaja?ii pe raioane, care au coinciden?? între parametrii adresei: num?rul casei ?i num?rul apartamentului.
SELECT RAION,COUNT(*) AS ANGAJATI
	FROM ANGAJAT A INNER JOIN LOC_STR LS ON LS.LOC_STR_ID=A.LOC_STR_ID
	INNER JOIN LOCALITATE L ON L.LOCALITATE_ID=LS.LOCALITATE_ID
	INNER JOIN RAION R ON R.RAION_ID=L.RAION_ID
	GROUP BY RAION

--S? se scrie o interogare care va afi?a angaja?ii pe departamente(departament, func?ia, FNP, salariul) ordona?i dup? aceia?i parametri.
SELECT NUME+' '+PRENUME AS NAME,DENUMIRE,DENUMIRE_FUNCTIE,SALARIU
	FROM ANGAJAT A INNER JOIN ANGAJARE AA ON A.ANGAJAT_ID=AA.ANGAJAT_ID
	INNER JOIN FUNCTIE F ON F.FUNCTIE_ID=AA.FUNCTIE_ID
	INNER JOIN DEPARTAMENT D ON D.DEPARTAMENT_ID=AA.DEPARTAMENT_ID

--Scrie o interogare pentru a ob?ine datele statistice(raion, num?r departamente, num?r total angaja?i, num?r de unit??i, suma salariilor).
SELECT RAION,COUNT(DENUMIRE) AS NR_DEPARTAMENTE,COUNT(*) AS NR_ANGAJATI,SUM(SALARIU) AS SAL
	FROM ANGAJAT A INNER JOIN LOC_STR LS ON LS.LOC_STR_ID=A.LOC_STR_ID
	INNER JOIN LOCALITATE L ON L.LOCALITATE_ID=LS.LOCALITATE_ID
	INNER JOIN RAION R ON R.RAION_ID=L.RAION_ID
	INNER JOIN ANGAJARE AA ON AA.ANGAJAT_ID=A.ANGAJAT_ID
	INNER JOIN DEPARTAMENT D ON D.DEPARTAMENT_ID=AA.DEPARTAMENT_ID
	GROUP BY RAION