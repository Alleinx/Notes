while getopts "tT" switches; do
    case "$switches" in
        t)
            echo 'Perform Training'
            python train.py --train=yes --test=no 
            # choice: 
            #   --prefix: storage file prefix.
            ;;
        T)
            echo 'Perform Test' 
			python train.py --train=No --test=yes
            ;;
        \?)
            echo -e "Invalid option: -$OPTARG."
            show_help
            exit 1
            ;;
    esac
done
