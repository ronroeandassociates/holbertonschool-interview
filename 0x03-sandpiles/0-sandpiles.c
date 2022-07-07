#include <stdio.h>
#include <stdlib.h>
#include "sandpiles.h"

/**
 * sandpiles_sum - sums two sandpiles and topples until sum is stable
 * @grid1: first sandpile
 * @grid2: second sandpile
 *
 */
void sandpiles_sum(int grid1[3][3],
									 int grid2[3][3])
{
	int col, row;
	int flags[3][3] = {
			{0, 0, 0},
			{0, 0, 0},
			{0, 0, 0}};

	/* sum the two grids */
	for (row = 0; row < 3; row++)
	{
		for (col = 0; col < 3; col++)
		{
			grid1[row][col] += grid2[row][col];
		}
	}

	while (checkStablility(grid1, flags))
	{
		/* print before toppling */
		printf("=\n");
		print_grid(grid1);

		/* every flag, topple cell */
		for (row = 0; row < 3; row++)
		{
			for (col = 0; col < 3; col++)
			{
				if (flags[row][col] == 1)
				{
					toppleCell(grid1, row, col);
				}
			}
		}
	}
}
