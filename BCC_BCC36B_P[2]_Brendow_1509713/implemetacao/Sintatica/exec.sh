for file in ./teste/*.tpp
  do
    python3 ./tppparser.py $file
    read -p "Pressione ENTER para continuar"
    echo ""
  done