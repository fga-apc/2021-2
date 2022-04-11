#include <stdio.h>

int ack(m, n)
int m, n;
{
    int ans;
    if (m == 0)
        ans = n + 1;
    else if (n == 0)
        ans = ack(m - 1, 1);
    else
        ans = ack(m - 1, ack(m, n - 1));
    return (ans);
}
