import sys

import matplotlib.pyplot as plt
from astropy.io import fits
from astropy.wcs import WCS
import numpy as np

moment0_file = snakemake.input[0]
outputfile = "results/plots/moment0_map.png"

hdu = fits.open(moment0_file)[0]
wcs = WCS(hdu.header)


# Initiate a figure and axis object with WCS projection information
fig = plt.figure()
ax = fig.add_subplot(111, projection = wcs)


# Display the moment map image
mask_threshold = 350
my_viridis = plt.colormaps.get_cmap('viridis_r').with_extremes(under='white')
im = ax.imshow(hdu.data, cmap = my_viridis, vmin = mask_threshold, vmax=2.2e3, origin = 'lower')


# Select region to plot
central_pixel_x = 512
central_pixel_y = 413
deg_per_pixel = 0.000416666676800
span = 0.25 / deg_per_pixel


# Overlay contours
plt.contour(
    hdu.data,
    levels=mask_threshold * np.array([1, 2, 3]),
    colors='black',
    alpha=0.5,
)


# Add a colorbar
cbar = plt.colorbar(im, pad=.07)
cbar.set_label('Velocity (km/s)', size=16)


# Set label
ax.set( xlim = (central_pixel_x - span / 2, central_pixel_x + span / 2),
        ylim = (central_pixel_y - span / 2, central_pixel_y + span / 2),
        xlabel = 'Right Ascension',
        ylabel = 'Declination',
        title = 'MOMENT 0 MAP')
plt.grid(color='black', alpha=0.25, ls='solid')

plt.savefig(outputfile, bbox_inches='tight', dpi=200)
