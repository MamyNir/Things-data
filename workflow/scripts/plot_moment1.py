import matplotlib.pyplot as plt
from astropy.wcs import WCS
from astropy.io import fits


moment1_file = snakemake.input[0]
outputfile = "results/plots/moment1_map.png"

hdu = fits.open(moment1_file)[0]
wcs = WCS(hdu)

# Initiate figure and axis
fig = plt.figure()
ax = fig.add_subplot(111, projection = wcs)

# Display the moment map
im = ax.imshow(hdu.data, cmap = "viridis_r")


# Add colorabar
cbar = plt.colorbar(im,pad = .07)
cbar.set_label("Rest Frequency (Hz)", fontsize = 16)


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
        title = 'MOMENT 1 MAP')
plt.grid(color='black', alpha=0.25, ls='solid')

# Overlay contours
plt.contour(hdu.data, colors='black', alpha=0.5)

# Save figure
plt.savefig(outputfile, bbox_inches='tight', dpi=200)
