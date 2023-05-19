#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: RFID SNR Frequency Hopping
# Author: Nahid
# GNU Radio version: 3.10.4.0

from packaging.version import Version as StrictVersion

if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print("Warning: failed to XInitThreads()")

from PyQt5 import Qt
from gnuradio import eng_notation
from gnuradio import analog
from gnuradio import blocks
from gnuradio import filter
from gnuradio.filter import firdes
from gnuradio import gr
from gnuradio.fft import window
import sys
import signal
from argparse import ArgumentParser
from gnuradio.eng_arg import eng_float, intx
import RFID_SNR_Frequency_Hopping_python_module_4Frequency as python_module_4Frequency  # embedded python module
import time
import threading



from gnuradio import qtgui

class RFID_SNR_Frequency_Hopping(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "RFID SNR Frequency Hopping", catch_exceptions=True)
        Qt.QWidget.__init__(self)
        self.setWindowTitle("RFID SNR Frequency Hopping")
        qtgui.util.check_set_qss()
        try:
            self.setWindowIcon(Qt.QIcon.fromTheme('gnuradio-grc'))
        except:
            pass
        self.top_scroll_layout = Qt.QVBoxLayout()
        self.setLayout(self.top_scroll_layout)
        self.top_scroll = Qt.QScrollArea()
        self.top_scroll.setFrameStyle(Qt.QFrame.NoFrame)
        self.top_scroll_layout.addWidget(self.top_scroll)
        self.top_scroll.setWidgetResizable(True)
        self.top_widget = Qt.QWidget()
        self.top_scroll.setWidget(self.top_widget)
        self.top_layout = Qt.QVBoxLayout(self.top_widget)
        self.top_grid_layout = Qt.QGridLayout()
        self.top_layout.addLayout(self.top_grid_layout)

        self.settings = Qt.QSettings("GNU Radio", "RFID_SNR_Frequency_Hopping")

        try:
            if StrictVersion(Qt.qVersion()) < StrictVersion("5.0.0"):
                self.restoreGeometry(self.settings.value("geometry").toByteArray())
            else:
                self.restoreGeometry(self.settings.value("geometry"))
        except:
            pass

        ##################################################
        # Variables
        ##################################################
        self.power_measure = power_measure = 0
        self.noise_measure = noise_measure = 0
        self.function_probe = function_probe = 0
        self.carrier_frequency = carrier_frequency = python_module_4Frequency.sweeper(function_probe)
        self.Level_Gauge_0 = Level_Gauge_0 = noise_measure
        self.Level_Gauge = Level_Gauge = power_measure
        self.Length_Mov_AVG = Length_Mov_AVG = 1024*20
        self.samp_rate = samp_rate = 10e6
        self.poll_rate = poll_rate = 0.5
        self.noOfItems = noOfItems = 1024*200
        self.frequency = frequency = carrier_frequency
        self.freq = freq = 1e6
        self.filter_shift = filter_shift = 0.01e6
        self.Level_Gauge_1 = Level_Gauge_1 = (Level_Gauge-Level_Gauge_0)
        self.Length_Mov_AVG_INV = Length_Mov_AVG_INV = 1/Length_Mov_AVG

        ##################################################
        # Blocks
        ##################################################
        self.probe_signal = blocks.probe_signal_c()
        self.power = blocks.probe_signal_f()
        self.noise = blocks.probe_signal_f()
        def _power_measure_probe():
          while True:

            val = self.power.level()
            try:
              try:
                self.doc.add_next_tick_callback(functools.partial(self.set_power_measure,val))
              except AttributeError:
                self.set_power_measure(val)
            except AttributeError:
              pass
            time.sleep(1.0 / (poll_rate))
        _power_measure_thread = threading.Thread(target=_power_measure_probe)
        _power_measure_thread.daemon = True
        _power_measure_thread.start()
        def _noise_measure_probe():
          while True:

            val = self.noise.level()
            try:
              try:
                self.doc.add_next_tick_callback(functools.partial(self.set_noise_measure,val))
              except AttributeError:
                self.set_noise_measure(val)
            except AttributeError:
              pass
            time.sleep(1.0 / (poll_rate))
        _noise_measure_thread = threading.Thread(target=_noise_measure_probe)
        _noise_measure_thread.daemon = True
        _noise_measure_thread.start()
        def _function_probe_probe():
          while True:

            val = self.probe_signal.level()
            try:
              try:
                self.doc.add_next_tick_callback(functools.partial(self.set_function_probe,val))
              except AttributeError:
                self.set_function_probe(val)
            except AttributeError:
              pass
            time.sleep(1.0 / (0.5))
        _function_probe_thread = threading.Thread(target=_function_probe_probe)
        _function_probe_thread.daemon = True
        _function_probe_thread.start()
        self._frequency_tool_bar = Qt.QToolBar(self)

        if None:
            self._frequency_formatter = None
        else:
            self._frequency_formatter = lambda x: eng_notation.num_to_str(x)

        self._frequency_tool_bar.addWidget(Qt.QLabel("Frequency[GHz]:  "))
        self._frequency_label = Qt.QLabel(str(self._frequency_formatter(self.frequency)))
        self._frequency_tool_bar.addWidget(self._frequency_label)
        self.top_layout.addWidget(self._frequency_tool_bar)
        self.blocks_nlog10_ff_0_0 = blocks.nlog10_ff(10, 1, 0)
        self.blocks_nlog10_ff_0 = blocks.nlog10_ff(10, 1, 0)
        self.blocks_moving_average_xx_0_0_0_0 = blocks.moving_average_ff(int(Length_Mov_AVG), Length_Mov_AVG_INV, (10*int(Length_Mov_AVG)), 1)
        self.blocks_moving_average_xx_0_0_0 = blocks.moving_average_ff(int(Length_Mov_AVG), Length_Mov_AVG_INV, (10*int(Length_Mov_AVG)), 1)
        self.blocks_complex_to_mag_squared_0_0_0_0 = blocks.complex_to_mag_squared(1)
        self.blocks_complex_to_mag_squared_0_0_0 = blocks.complex_to_mag_squared(1)
        self.band_pass_filter_0_0 = filter.fir_filter_ccf(
            1,
            firdes.band_pass(
                1,
                samp_rate,
                (freq-filter_shift*2),
                (freq-filter_shift),
                (filter_shift/2),
                window.WIN_HAMMING,
                6.76))
        self.band_pass_filter_0 = filter.fir_filter_ccf(
            1,
            firdes.band_pass(
                1,
                samp_rate,
                (freq-filter_shift),
                (freq+filter_shift),
                (filter_shift/2),
                window.WIN_HAMMING,
                6.76))
        self.analog_sig_source_x_0_0 = analog.sig_source_c(samp_rate, analog.GR_COS_WAVE, freq, 1, 0, 0)
        self.analog_sig_source_x_0 = analog.sig_source_c(samp_rate, analog.GR_COS_WAVE, carrier_frequency, 1, 0, 0)
        self._Level_Gauge_1_tool_bar = Qt.QToolBar(self)

        if None:
            self._Level_Gauge_1_formatter = None
        else:
            self._Level_Gauge_1_formatter = lambda x: eng_notation.num_to_str(x)

        self._Level_Gauge_1_tool_bar.addWidget(Qt.QLabel("Absolute Power[dB]:  "))
        self._Level_Gauge_1_label = Qt.QLabel(str(self._Level_Gauge_1_formatter(self.Level_Gauge_1)))
        self._Level_Gauge_1_tool_bar.addWidget(self._Level_Gauge_1_label)
        self.top_layout.addWidget(self._Level_Gauge_1_tool_bar)
        self._Level_Gauge_0_tool_bar = Qt.QToolBar(self)

        if None:
            self._Level_Gauge_0_formatter = None
        else:
            self._Level_Gauge_0_formatter = lambda x: eng_notation.num_to_str(x)

        self._Level_Gauge_0_tool_bar.addWidget(Qt.QLabel("Noise[dB]: "))
        self._Level_Gauge_0_label = Qt.QLabel(str(self._Level_Gauge_0_formatter(self.Level_Gauge_0)))
        self._Level_Gauge_0_tool_bar.addWidget(self._Level_Gauge_0_label)
        self.top_layout.addWidget(self._Level_Gauge_0_tool_bar)
        self._Level_Gauge_tool_bar = Qt.QToolBar(self)

        if None:
            self._Level_Gauge_formatter = None
        else:
            self._Level_Gauge_formatter = lambda x: eng_notation.num_to_str(x)

        self._Level_Gauge_tool_bar.addWidget(Qt.QLabel("Power[dB]:  "))
        self._Level_Gauge_label = Qt.QLabel(str(self._Level_Gauge_formatter(self.Level_Gauge)))
        self._Level_Gauge_tool_bar.addWidget(self._Level_Gauge_label)
        self.top_layout.addWidget(self._Level_Gauge_tool_bar)


        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_sig_source_x_0, 0), (self.band_pass_filter_0, 0))
        self.connect((self.analog_sig_source_x_0, 0), (self.band_pass_filter_0_0, 0))
        self.connect((self.analog_sig_source_x_0_0, 0), (self.probe_signal, 0))
        self.connect((self.band_pass_filter_0, 0), (self.blocks_complex_to_mag_squared_0_0_0, 0))
        self.connect((self.band_pass_filter_0_0, 0), (self.blocks_complex_to_mag_squared_0_0_0_0, 0))
        self.connect((self.blocks_complex_to_mag_squared_0_0_0, 0), (self.blocks_moving_average_xx_0_0_0, 0))
        self.connect((self.blocks_complex_to_mag_squared_0_0_0_0, 0), (self.blocks_moving_average_xx_0_0_0_0, 0))
        self.connect((self.blocks_moving_average_xx_0_0_0, 0), (self.blocks_nlog10_ff_0, 0))
        self.connect((self.blocks_moving_average_xx_0_0_0_0, 0), (self.blocks_nlog10_ff_0_0, 0))
        self.connect((self.blocks_nlog10_ff_0, 0), (self.power, 0))
        self.connect((self.blocks_nlog10_ff_0_0, 0), (self.noise, 0))


    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "RFID_SNR_Frequency_Hopping")
        self.settings.setValue("geometry", self.saveGeometry())
        self.stop()
        self.wait()

        event.accept()

    def get_power_measure(self):
        return self.power_measure

    def set_power_measure(self, power_measure):
        self.power_measure = power_measure
        self.set_Level_Gauge(self.power_measure)

    def get_noise_measure(self):
        return self.noise_measure

    def set_noise_measure(self, noise_measure):
        self.noise_measure = noise_measure
        self.set_Level_Gauge_0(self.noise_measure)

    def get_function_probe(self):
        return self.function_probe

    def set_function_probe(self, function_probe):
        self.function_probe = function_probe
        self.set_carrier_frequency(python_module_4Frequency.sweeper(self.function_probe))

    def get_carrier_frequency(self):
        return self.carrier_frequency

    def set_carrier_frequency(self, carrier_frequency):
        self.carrier_frequency = carrier_frequency
        self.set_frequency(self.carrier_frequency)
        self.analog_sig_source_x_0.set_frequency(self.carrier_frequency)

    def get_Level_Gauge_0(self):
        return self.Level_Gauge_0

    def set_Level_Gauge_0(self, Level_Gauge_0):
        self.Level_Gauge_0 = Level_Gauge_0
        Qt.QMetaObject.invokeMethod(self._Level_Gauge_0_label, "setText", Qt.Q_ARG("QString", str(self._Level_Gauge_0_formatter(self.Level_Gauge_0))))
        self.set_Level_Gauge_1((self.Level_Gauge-self.Level_Gauge_0))

    def get_Level_Gauge(self):
        return self.Level_Gauge

    def set_Level_Gauge(self, Level_Gauge):
        self.Level_Gauge = Level_Gauge
        Qt.QMetaObject.invokeMethod(self._Level_Gauge_label, "setText", Qt.Q_ARG("QString", str(self._Level_Gauge_formatter(self.Level_Gauge))))
        self.set_Level_Gauge_1((self.Level_Gauge-self.Level_Gauge_0))

    def get_Length_Mov_AVG(self):
        return self.Length_Mov_AVG

    def set_Length_Mov_AVG(self, Length_Mov_AVG):
        self.Length_Mov_AVG = Length_Mov_AVG
        self.set_Length_Mov_AVG_INV(1/self.Length_Mov_AVG)
        self.blocks_moving_average_xx_0_0_0.set_length_and_scale(int(self.Length_Mov_AVG), self.Length_Mov_AVG_INV)
        self.blocks_moving_average_xx_0_0_0_0.set_length_and_scale(int(self.Length_Mov_AVG), self.Length_Mov_AVG_INV)

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.analog_sig_source_x_0.set_sampling_freq(self.samp_rate)
        self.analog_sig_source_x_0_0.set_sampling_freq(self.samp_rate)
        self.band_pass_filter_0.set_taps(firdes.band_pass(1, self.samp_rate, (self.freq-self.filter_shift), (self.freq+self.filter_shift), (self.filter_shift/2), window.WIN_HAMMING, 6.76))
        self.band_pass_filter_0_0.set_taps(firdes.band_pass(1, self.samp_rate, (self.freq-self.filter_shift*2), (self.freq-self.filter_shift), (self.filter_shift/2), window.WIN_HAMMING, 6.76))

    def get_poll_rate(self):
        return self.poll_rate

    def set_poll_rate(self, poll_rate):
        self.poll_rate = poll_rate

    def get_noOfItems(self):
        return self.noOfItems

    def set_noOfItems(self, noOfItems):
        self.noOfItems = noOfItems

    def get_frequency(self):
        return self.frequency

    def set_frequency(self, frequency):
        self.frequency = frequency
        Qt.QMetaObject.invokeMethod(self._frequency_label, "setText", Qt.Q_ARG("QString", str(self._frequency_formatter(self.frequency))))

    def get_freq(self):
        return self.freq

    def set_freq(self, freq):
        self.freq = freq
        self.analog_sig_source_x_0_0.set_frequency(self.freq)
        self.band_pass_filter_0.set_taps(firdes.band_pass(1, self.samp_rate, (self.freq-self.filter_shift), (self.freq+self.filter_shift), (self.filter_shift/2), window.WIN_HAMMING, 6.76))
        self.band_pass_filter_0_0.set_taps(firdes.band_pass(1, self.samp_rate, (self.freq-self.filter_shift*2), (self.freq-self.filter_shift), (self.filter_shift/2), window.WIN_HAMMING, 6.76))

    def get_filter_shift(self):
        return self.filter_shift

    def set_filter_shift(self, filter_shift):
        self.filter_shift = filter_shift
        self.band_pass_filter_0.set_taps(firdes.band_pass(1, self.samp_rate, (self.freq-self.filter_shift), (self.freq+self.filter_shift), (self.filter_shift/2), window.WIN_HAMMING, 6.76))
        self.band_pass_filter_0_0.set_taps(firdes.band_pass(1, self.samp_rate, (self.freq-self.filter_shift*2), (self.freq-self.filter_shift), (self.filter_shift/2), window.WIN_HAMMING, 6.76))

    def get_Level_Gauge_1(self):
        return self.Level_Gauge_1

    def set_Level_Gauge_1(self, Level_Gauge_1):
        self.Level_Gauge_1 = Level_Gauge_1
        Qt.QMetaObject.invokeMethod(self._Level_Gauge_1_label, "setText", Qt.Q_ARG("QString", str(self._Level_Gauge_1_formatter(self.Level_Gauge_1))))

    def get_Length_Mov_AVG_INV(self):
        return self.Length_Mov_AVG_INV

    def set_Length_Mov_AVG_INV(self, Length_Mov_AVG_INV):
        self.Length_Mov_AVG_INV = Length_Mov_AVG_INV
        self.blocks_moving_average_xx_0_0_0.set_length_and_scale(int(self.Length_Mov_AVG), self.Length_Mov_AVG_INV)
        self.blocks_moving_average_xx_0_0_0_0.set_length_and_scale(int(self.Length_Mov_AVG), self.Length_Mov_AVG_INV)




def main(top_block_cls=RFID_SNR_Frequency_Hopping, options=None):

    if StrictVersion("4.5.0") <= StrictVersion(Qt.qVersion()) < StrictVersion("5.0.0"):
        style = gr.prefs().get_string('qtgui', 'style', 'raster')
        Qt.QApplication.setGraphicsSystem(style)
    qapp = Qt.QApplication(sys.argv)

    tb = top_block_cls()

    tb.start()

    tb.show()

    def sig_handler(sig=None, frame=None):
        tb.stop()
        tb.wait()

        Qt.QApplication.quit()

    signal.signal(signal.SIGINT, sig_handler)
    signal.signal(signal.SIGTERM, sig_handler)

    timer = Qt.QTimer()
    timer.start(500)
    timer.timeout.connect(lambda: None)

    qapp.exec_()

if __name__ == '__main__':
    main()
