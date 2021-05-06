service Calculadora{
   void ping(),
   i32 suma(1:i32 num1, 2:i32 num2),
   i32 resta(1:i32 num1, 2:i32 num2),
   i32 multiplicacion(1:i32 num1, 2:i32 num2),
   i32 division(1:i32 num1, 2:i32 num2),

   list<i32> suma_vectores(1:list<i32> v1, 2:list<i32> v2),
   list<i32> resta_vectores(1:list<i32> v1, 2:list<i32> v2),
   list<i32> multiplicacion_vectores(1:list<i32> v1, 2:list<i32> v2),

   list<list<i32>> multiplicacion_matrices(1:list<list<i32>> m1, 2:list<list<i32>> m2),
}
