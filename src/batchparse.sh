if [ "$#" -ne 1 ]; then
	    echo "Invalid Number of Arguments:\nYou must indicate the folder holding the data as an input argument"
	    exit
fi
mkdir csvdump
> parserlog
for xml in `find $1 -name *.xml`
do
	python xmlparser.py $xml csvdump >> parserlog
	csvfile="$xml"".csv"
	echo $csvfile
	mv $csvfile csvdump
done
