#include "menger.h"

/**
 * menger - draws a 2D Menger Sponge
 * @level: level of the Menger Sponge to draw
 */

void menger(int level)
{
	int size, x, y, i, j, k, l;

	if (level < 0)
		return;

	size = pow(3, level);
	for (x = 0; x < size; x++)
	{
		for (y = 0; y < size; y++)
		{
			i = x;
			j = y;
			while (i > 0 || j > 0)
			{
				k = i % 3;
				l = j % 3;
				if (k == 1 && l == 1)
				{
					printf(" ");
					break;
				}
				i /= 3;
				j /= 3;
			}
			if (i == 0 && j == 0)
				printf("#");
		}
		printf("\n");
	}
}
