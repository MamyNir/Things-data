
import matplotlib.pyplot as plt
from astropy.io import fits
from astropy.wcs import WCS

moment2_file = snakemake.input[0]
outputfile = "results/plots/moment2_map.png"


hdu = fits.open(moment2_file)[0]
wcs = WCS(hdu)

# Initiate figure and axes
fig = plt.figure()
ax = fig.add_subplot(111, projection = wcs)


# Display the moment map image
my_viridis = plt.colormaps.get_cmap('viridis_r').with_extremes(under='white')
im = ax.imshow(hdu.data, cmap = my_viridis, vmin = 2e4, vmax=14e4, origin = 'lower')


# Select region to plot
central_pixel_x = 512
central_pixel_y = 413
deg_per_pixel = 0.000416666676800
span = 0.32 / deg_per_pixel


# Set label
ax.set( xlim = (central_pixel_x - span / 2, central_pixel_x + span / 2),
        ylim = (central_pixel_y - span / 2, central_pixel_y + span / 2),
        xlabel = 'Right Ascension (J2000)',
        ylabel = 'Declination (J2000)',
        title = 'MOMENT 2 MAP')
plt.grid(color='black', alpha=0.25, ls='solid')

# Add colorabar
cbar = plt.colorbar(im,pad = .1)
cbar.set_label("Temperature (K)", fontsize = 16)


# Save figure
plt.savefig(outputfile, bbox_inches='tight', dpi=200)
