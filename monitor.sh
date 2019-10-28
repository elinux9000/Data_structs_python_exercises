unset parms
evince ~/Downloads/algos_python.pdf &>>/dev/null &

for p in $@
do
	parms=$parms" "$p
done
echo "Args:"$parms

ls *.py > cscope.files

pgrep --count inotifywait >>/dev/null
if [ $? -eq 1 ]; then
	    echo no other inotifywait running
	    else
		echo "inotifywait is running"
		echo "continue?(y)"
		read a
		if [ $a != "y" ];then
			exit
		fi
fi

if [ -z "$1" ]; then
	echo "Usage: monitor FILENAME"
	exit
fi


while true; do
	echo "Waiting"
	inotifywait -e modify *.py
	clear && printf '\e[3J'
	cscope -b
	#yapf --style style.yapf -i *.py && echo "Executing" && python test_blending.py
	yapf --style ../style.yapf -i *.py 
	echo "Executing" && python $parms
done

