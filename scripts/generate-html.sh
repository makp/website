#!/bin/sh


config_path=$2 			# path to htlatex config

# The function below only takes one argument: the path to tex file. It
# copies this file to a folder in /tmp/, converts it to an html file,
# and copies it back to the folder where the tex file was.

produce_html ()
{
    base=$(echo "$1" | sed -r "s/.+\/(.+)\..+/\1/") # store basename
    temp_folder=/tmp/website_$base
    if [ -d "$temp_folder" ]; then
	rm -r $temp_folder
    fi
    mkdir $temp_folder
    cp $1 $temp_folder && cd $temp_folder
    latex $base
    biber $base
    # read -n 1 -p ">>>>> 'biber $base' finished. Press ENTER to continue..."
    htlatex $base "$config_path,-css,NoFonts"
    # read -n 1 -p ">>>>> 'htlatex $base' finished. Press ENTER to continue..."
    mv $base.html $(dirname $1)
}

produce_html $1
