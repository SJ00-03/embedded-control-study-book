#include <stddef.h>
#include <stdio.h>

static void set_speed_by_pointer(int *speed_rpm)
{
    if (speed_rpm == NULL) {
        return;
    }

    *speed_rpm = 1500;
}

static int average_i32(const int *samples, size_t count, int *out_avg)
{
    long sum = 0;

    if (samples == NULL || out_avg == NULL || count == 0U) {
        return -1;
    }

    for (size_t i = 0; i < count; ++i) {
        sum += samples[i];
    }

    *out_avg = (int)(sum / (long)count);
    return 0;
}

int main(void)
{
    int motor_speed_rpm = 1200;
    int adc_samples[] = {100, 120, 130, 150, 170};
    int average = 0;
    const size_t sample_count = sizeof(adc_samples) / sizeof(adc_samples[0]);

    printf("initial speed: %d rpm\n", motor_speed_rpm);
    set_speed_by_pointer(&motor_speed_rpm);
    printf("updated speed: %d rpm\n", motor_speed_rpm);

    if (average_i32(adc_samples, sample_count, &average) == 0) {
        printf("sample average: %d\n", average);
    } else {
        printf("sample average: error\n");
    }

    if (average_i32(NULL, sample_count, &average) != 0) {
        printf("null input check: rejected\n");
    }

    return 0;
}
