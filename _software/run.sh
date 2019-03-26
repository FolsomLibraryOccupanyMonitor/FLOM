python manage.py runserver

# use "sh run.sh"
# if you use python3, do "sh run.sh 3"

for i in "$*"
do
	echo "\n*** use 'sh run.sh 3' to run using python3 ***"
	echo "*** Using python" $i "***\n"
done

if [ "$*" == "3" ]
then
	python3 manage.py runserver 0.0.0.0:80
else
    python manage.py runserver 0.0.0.0:80
fi