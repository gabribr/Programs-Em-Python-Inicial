int cont = 11,d1,d2,d3,d4,d5,d6,d7,d8,d9,d10,d11,calc1,calc2,dv1,dv2;

long cpf;
Console.WriteLine("Digite seu cpf: ");
cpf= long.Parse(Console.ReadLine());
while (cont > 0)
{
    switch (cont)
    {
case 1:  cpf = cpf/10; d1  = (int)(cpf % 10); break;
case 2:  cpf = cpf/10; d2  = (int)(cpf % 10); break;
case 3:  cpf = cpf/10; d3  = (int)(cpf % 10); break;
case 4:  cpf = cpf/10; d4  = (int)(cpf % 10); break;
case 5:  cpf = cpf/10; d5  = (int)(cpf % 10); break;
case 6:  cpf = cpf/10; d6  = (int)(cpf % 10); break;
case 7:  cpf = cpf/10; d7  = (int)(cpf % 10); break;
case 8:  cpf = cpf/10; d8  = (int)(cpf % 10); break;
case 9:  cpf = cpf/10; d9  = (int)(cpf % 10); break;
case 10: cpf = cpf/10; d10 = (int)(cpf % 10); break;
case 11: cpf = cpf/10; d11 = (int)(cpf % 10); break;
        default:
    }
    cont--;    
}
calc1 = (d1*10)+(d2*9)+(d3*8)+(d4*7)+(d5*6)+(d6*5)+(d7*4)+(d8*3)+(d9*2);
if(calc1 % 11 < 2){
dv1 = 0;
}
else
{
    dv1 = 11- (calc1%11);
}
if(dv1 == d10) {
calc2 = (d1*11)+(d2*10)+(d3*9)+(d4*8)+(d5*7)+(d6*6)+(d7*5)+(d8*4)+(d9*3)+(dv1*2);
if( calc2 % 11 < 2){
dv2 = 0;
}
else
{
    dv2 = 11-(calc2%11);
}
if(dv2 == d11){
    Console.WriteLine("cpf valido");
}
else{
    Console.WriteLine("Cpf Invalido ");
}

}
else{
    Console.WriteLine("Cpf Invalido ");
}