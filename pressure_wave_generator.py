import numpy as np
from pathlib import Path
from csv_to_xml import generate_ANSYS_xml_parameter


def write_string_to_file(string, output_file):
    with open(output_file, "w") as file:
        file.write(string)


timesteps = 25
t_0 = 0  # s
t_k = 10e-6  # s
t_f = 100e-6  # s
t_c = 12.5e-6  # s
P_peak = 900e6  # Pa
P_0 = 100e6  # Pa

t_decay = np.linspace(t_0, t_f - t_k, int(timesteps * (1 - t_k / t_f)))
t_const = np.linspace(t_0, t_k, int(timesteps * (t_k / t_f)) + 1)[:-1]

P_decay = (P_peak - P_0) * np.exp(-t_decay / t_c) + P_0
P_const = np.ones(len(t_const)) * P_peak

t = np.concatenate((t_const, t_decay + t_k))
Pi = np.concatenate((P_const, P_decay))

output_data = np.vstack((t, Pi)).T

# output = Path(__file__).resolve().parent / "output.csv"
# np.savetxt(output, output_data, delimiter=',')

output = Path(__file__).resolve().parent / "output.xml"
xml = generate_ANSYS_xml_parameter(t.tolist(), Pi.tolist(), ("Time", "Pressure"))
write_string_to_file(xml, output)
