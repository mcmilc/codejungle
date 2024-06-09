/* From Book: Algorithmic Thinking - Daniel Zingaro (Chapter 1)
Example:

   Line 1: 3
   Line 2: 2
   Line 3: 5

   4 new people arrive.

   1) Line 2: 3
   2) Line 1: 4
   3) Line 2: 4
   4) Line 1: 5

   1) Person 1 joins Line 2 -> 3 left
   2) Person 2 joins Line 1 -> 2 left
   3) Person 3 joins Line 2 -> 1 left
   4) Person 4 joins Line 1 -> 0 left
*/
#include <stdio.h>
// return the line-index with the shortest number of people
int shortest_line_index(int lines[], int n_lines);
void join_line(int lines[], int n, int m);

int shortest_line_index(int lines[], int n_lines)
{
    int idx;
    int shortest = 0;
    for (idx = 0; idx < n_lines; idx++)
    {
        if (lines[idx] < lines[shortest])
        {
            shortest = idx;
        }
    }
    return shortest;
}

void join_line(int lines[], int n, int m)
{
    int idx;
    for (int next = 0; next < m; next++)
    {
        idx = shortest_line_index(lines, n);
        lines[idx]++;
    }
}

int main()
{
    int N_LINES = 3;
    int lines[3] = {3, 2, 5};
    join_line(lines, N_LINES, 4);
    for (int i = 0; i < N_LINES; i++)
    {
        printf("Line %d: %d\n", i + 1, lines[i]);
    }
    return 0;
}