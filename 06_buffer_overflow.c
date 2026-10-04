/* Experiment 6: Buffer Overflow Vulnerability (educational demonstration)
   A small buffer sits next to an 'authenticated' flag inside the same
   structure. An unchecked strcpy() overflows the buffer and silently
   changes the flag, granting access without a valid password.        */
#include <stdio.h>
#include <string.h>
#include <stddef.h>

struct frame {
    char buffer[8];          /* user input is copied here          */
    int  authenticated;      /* 0 = access denied, non-zero = granted */
};

void vulnerable(const char *input) {
    struct frame f;
    f.authenticated = 0;
    strcpy(f.buffer, input);                 /* NO bounds checking */
    printf("  Input length    : %zu characters\n", strlen(input));
    printf("  authenticated   : 0x%08x\n", f.authenticated);
    printf("  Result          : %s\n",
           f.authenticated ? "ACCESS GRANTED (flag corrupted!)" : "Access denied");
}

void secure(const char *input) {
    struct frame f;
    f.authenticated = 0;
    if (strlen(input) >= sizeof(f.buffer)) {          /* bounds check */
        printf("  Input length    : %zu characters\n", strlen(input));
        printf("  Result          : Input rejected (too long) - overflow prevented\n");
        return;
    }
    strcpy(f.buffer, input);
    printf("  authenticated   : 0x%08x\n", f.authenticated);
    printf("  Result          : Access denied\n");
}

int main(void) {
    printf("Layout: buffer at offset %zu (size %zu), flag at offset %zu\n\n",
           offsetof(struct frame, buffer), sizeof(((struct frame *)0)->buffer),
           offsetof(struct frame, authenticated));

    printf("[1] Vulnerable program, normal input \"Hello\"\n");
    vulnerable("Hello");
    printf("\n[2] Vulnerable program, oversized input (11 x 'A')\n");
    vulnerable("AAAAAAAAAAA");
    printf("\n[3] Secure program, oversized input (11 x 'A')\n");
    secure("AAAAAAAAAAA");
    return 0;
}
