from flojoy import DataContainer, flojoy
import scipy.stats


@flojoy
def ZSCORE(dc, params):
    """

            Compute the z score.

            Compute the z score of each value in the sample, relative to the
            sample mean and standard deviation.

    -.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.
    The parameters of the function in this Flojoy wrapper are given below.
    -.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.

    Parameters
    ----------
    a : array_like
            An array like object containing the sample data.
    axis : int or None, optional
            Axis along which to operate. Default is 0. If None, compute over
            the whole array `a`.
    ddof : int, optional
            Degrees of freedom correction in the calculation of the
            standard deviation. Default is 0.
    nan_policy : {'propagate', 'raise', 'omit'}, optional
            Defines how to handle when input contains nan. 'propagate' returns nan,
            'raise' throws an error, 'omit' performs the calculations ignoring nan
            values. Default is 'propagate'.  Note that when the value is 'omit',
            nans in the input also propagate to the output, but they do not affect
            the z-scores computed for the non-nan values.
    """
    return DataContainer(
        x=dc[0].y,
        y=scipy.stats.zscore(
            a=dc[0].y,
            axis=(int(params["axis"]) if params["axis"] != "" else None),
            ddof=(int(params["ddof"]) if params["ddof"] != "" else None),
            nan_policy=(
                str(params["nan_policy"]) if params["nan_policy"] != "" else None
            ),
        ),
    )
