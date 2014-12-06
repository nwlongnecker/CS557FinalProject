mkdir $1

openssl req -newkey rsa:2048 -keyout $1/$1.key -config ../CA/openssl.cnf -out $1/$1.req
cd ../CA
openssl ca -config openssl.cnf -out ../entities/$1/$1.crt -infiles ../entities/$1/$1.req

# All passwords are 'pass'