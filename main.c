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

    for (int i = 0; i < 10; i++) {
        printf("%d\n", i);
    }

    printf("ветка retro\n");

    return 0;
}