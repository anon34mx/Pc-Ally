using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace PCAllySource
{
    internal class MouseUpdate
    {
        public string Method
        {
            get;
            set;
        }

        public Object Data
        {
            get;
            set;
        }
    }

    internal class Coords
    {
        public Coords()
        {
            //this.X = 0;
            //this.Y = 0;
        }
        public float X
        {
            get;
            set;
        }
        public float Y
        {
            get;
            set;
        }
    }
}
