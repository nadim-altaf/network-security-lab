#include <stdio.h>
#include <string.h>

struct data {
    char buffer[8];
    int authenticated;
};

void vulnerable(char *input) {
    struct data d;
    d.authenticated = 0;
    strcpy(d.buffer, input);
    printf("  Input length    : %d characters\n", (int)strlen(input));
    printf("  authenticated   : 0x%08x\n", d.authenticated);
    if (d.authenticated != 0)
        printf("  Result          : ACCESS GRANTED (flag corrupted!)\n");
    else
        printf("  Result          : Access denied\n");
}

void secure(char *input) {
    struct data d;
    d.authenticated = 0;
    if (strlen(input) >= sizeof(d.buffer)) {
        printf("  Input length    : %d characters\n", (int)strlen(input));
        printf("  Result          : Input rejected (too long) - overflow prevented\n");
        return;
    }
    strcpy(d.buffer, input);
    printf("  authenticated   : 0x%08x\n", d.authenticated);
    printf("  Result          : Access denied\n");
}

int main() {
    printf("Buffer size = 8 bytes, the flag is stored right after the buffer\n\n");

    printf("[1] Vulnerable program, normal input \"Hello\"\n");
    vulnerable("Hello");

    printf("\n[2] Vulnerable program, oversized input (11 x 'A')\n");
    vulnerable("AAAAAAAAAAA");

    printf("\n[3] Secure program, oversized input (11 x 'A')\n");
    secure("AAAAAAAAAAA");

    return 0;
}
