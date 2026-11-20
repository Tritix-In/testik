#include <stdio.h>

int add(int x, int y) {
    int res = x + y;
    return res;
}

int main(void) {

    int a, b;

    a = 25;
    b = 30;
    int res = add(a, b);
    printf("%d\n", res);

    printf("Это изменение файла!!!\n");

    return 0;
}