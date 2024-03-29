using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using System.IO.Ports;
using System.Threading;
using System.Web.Services.Description;
using static System.Net.Mime.MediaTypeNames;
using Newtonsoft.Json;
using System.Runtime.InteropServices;
using System.Diagnostics;

namespace PCAllySource
{
    public partial class Form1 : Form
    {
        const uint MOUSEEVENTF_ABSOLUTE = 0x8000;
        const uint MOUSEEVENTF_LEFTDOWN = 0x0002;
        const uint MOUSEEVENTF_LEFTUP = 0x0004;
        const uint MOUSEEVENTF_MIDDLEDOWN = 0x0020;
        const uint MOUSEEVENTF_MIDDLEUP = 0x0040;
        const uint MOUSEEVENTF_MOVE = 0x0001;
        const uint MOUSEEVENTF_RIGHTDOWN = 0x0008;
        const uint MOUSEEVENTF_RIGHTUP = 0x0010;
        const uint MOUSEEVENTF_XDOWN = 0x0080;
        const uint MOUSEEVENTF_XUP = 0x0100;
        const uint MOUSEEVENTF_WHEEL = 0x0800;
        const uint MOUSEEVENTF_HWHEEL = 0x01000;
        const double mouseSpeed = 0.099;


        private bool serialPortClosed = false;
        private String[] availablePorts;
        private System.IO.Ports.SerialPort Port;
        Thread threadSerial;
        Thread threadMouse;
        System.Timers.Timer timerPosAsiento;
        private int serialPortErrors = 0;
        //Stopwatch deltaTime = new Stopwatch();
        public Form1()
        {
            InitializeComponent();

            Console.WriteLine("START");
            //searchDevice();
            serialDevicesList();
        }

        private void searchDevice()
        {
            Console.WriteLine("Ports found");
            availablePorts = SerialPort.GetPortNames();
            foreach (var port in availablePorts)
            {
                String command = "hola";
                Console.WriteLine(port.ToString());
                Console.WriteLine(command);

                System.IO.Ports.SerialPort tempPort;
                Port = new System.IO.Ports.SerialPort
                {
                    PortName = port.ToString(),
                    BaudRate = 9600,
                    ReadTimeout = 500
                };
                try
                {
                    Port.Open();
                    Console.WriteLine("Port " + port.ToString() + " opened");
                    Port.WriteLine(command);
                    string text = Port.ReadLine();
                    Console.WriteLine(text);
                    Port.Close();
                }
                catch (Exception e)
                {

                }
            }
        }

        private void serialDevicesList()
        {
            availablePorts = SerialPort.GetPortNames();
            serialDevices.Items.AddRange(availablePorts);
        }
        public void OpenSerial(string portName)
        {
            try
            {
                if (Port != null)
                    Port.Close();
            }
            catch (Exception ex)
            {
                Console.WriteLine(ex);
            }
            try
            {
                Port = new System.IO.Ports.SerialPort
                {
                    PortName = portName,
                    BaudRate = 9600,
                    ReadTimeout = 500
                };
                Port.Open();
                Console.WriteLine("Port " + portName + " opened");
                threadSerial = new Thread(ListenSerial);
                threadSerial.Start();
                //Properties.Settings.Default.SerialPort = portName;
                //Properties.Settings.Default.Save();
                lbl_status_serial.Text = "Connected";
            }
            catch (Exception ex)
            {
                MessageBox.Show(ex.Message, "Error", MessageBoxButtons.OK);
                lbl_status_serial.Text = "Couldn't open";
            }
        }

        public async void ListenSerial()
        {
            while (!serialPortClosed)
            {
                //deltaTime.Start();
                try
                {
                    string text = Port.ReadLine();
                    Console.WriteLine("->" + text + "<-");
                    MouseUpdate mouseData = JsonConvert.DeserializeObject<MouseUpdate>(text);
                    var coords = JsonConvert.DeserializeObject<Coords>(mouseData.Data.ToString());
                    if (mouseData != null)
                    {
                        //Console.WriteLine("->" + mouseData.Method + "<-");
                        //Console.WriteLine("->" + mouseData.Data + "<-");
                        Console.WriteLine("-> X = " + Cursor.Position.X + " __  Y = " + Cursor.Position.Y + "<-");
                        Console.WriteLine("-> X = " + coords.X + "<--> Y = " + coords.Y + "<-\n");

                        Cursor.Position = new Point((int) (Cursor.Position.X + coords.X), (int) (Cursor.Position.Y + coords.Y));
                    }
                    //var x=new 
                }
                catch (Exception e)
                {

                }
                //deltaTime.Stop();
                //Console.WriteLine(deltaTime.ElapsedMilliseconds);
            }
        }



        // BUTTONS 
        private void searchDevice(object sender, EventArgs e) // button action
        {
            if (threadSerial!=null)
            {
                threadSerial.Abort();
            }
            threadSerial = new Thread(searchDevice);
            threadSerial.Start();
        }

        private void button2_Click(object sender, EventArgs e)
        {
            OpenSerial(serialDevices.Text);
        }

        [DllImport("user32.dll", CharSet = CharSet.Auto, CallingConvention = CallingConvention.StdCall)]
        public static extern void mouse_event(long dwFlags, long dx, long dy, long cButtons, long dwExtraInfo);

    }

}