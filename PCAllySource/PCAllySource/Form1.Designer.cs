namespace PCAllySource
{
    partial class Form1
    {
        /// <summary>
        /// Variable del diseñador necesaria.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// Limpiar los recursos que se estén usando.
        /// </summary>
        /// <param name="disposing">true si los recursos administrados se deben desechar; false en caso contrario.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Código generado por el Diseñador de Windows Forms

        /// <summary>
        /// Método necesario para admitir el Diseñador. No se puede modificar
        /// el contenido de este método con el editor de código.
        /// </summary>
        private void InitializeComponent()
        {
            this.label1 = new System.Windows.Forms.Label();
            this.button1 = new System.Windows.Forms.Button();
            this.serialDevices = new System.Windows.Forms.ComboBox();
            this.button2 = new System.Windows.Forms.Button();
            this.lbl_status_serial = new System.Windows.Forms.Label();
            this.SuspendLayout();
            // 
            // label1
            // 
            this.label1.AutoSize = true;
            this.label1.Location = new System.Drawing.Point(12, 9);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(40, 13);
            this.label1.TabIndex = 0;
            this.label1.Text = "PC Ally";
            // 
            // button1
            // 
            this.button1.Location = new System.Drawing.Point(420, 12);
            this.button1.Name = "button1";
            this.button1.Size = new System.Drawing.Size(186, 23);
            this.button1.TabIndex = 1;
            this.button1.Text = "Buscar dispositivos";
            this.button1.UseVisualStyleBackColor = true;
            // 
            // serialDevices
            // 
            this.serialDevices.FormattingEnabled = true;
            this.serialDevices.Location = new System.Drawing.Point(12, 48);
            this.serialDevices.Name = "serialDevices";
            this.serialDevices.Size = new System.Drawing.Size(185, 21);
            this.serialDevices.TabIndex = 2;
            // 
            // button2
            // 
            this.button2.Location = new System.Drawing.Point(222, 46);
            this.button2.Name = "button2";
            this.button2.Size = new System.Drawing.Size(75, 23);
            this.button2.TabIndex = 3;
            this.button2.Text = "Conectar";
            this.button2.UseVisualStyleBackColor = true;
            this.button2.Click += new System.EventHandler(this.button2_Click);
            // 
            // lbl_status_serial
            // 
            this.lbl_status_serial.AutoSize = true;
            this.lbl_status_serial.Location = new System.Drawing.Point(314, 51);
            this.lbl_status_serial.Name = "lbl_status_serial";
            this.lbl_status_serial.Size = new System.Drawing.Size(35, 13);
            this.lbl_status_serial.TabIndex = 4;
            this.lbl_status_serial.Text = "status";
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(618, 450);
            this.Controls.Add(this.lbl_status_serial);
            this.Controls.Add(this.button2);
            this.Controls.Add(this.serialDevices);
            this.Controls.Add(this.button1);
            this.Controls.Add(this.label1);
            this.Name = "Form1";
            this.Text = "Form1";
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.Label label1;
        private System.Windows.Forms.Button button1;
        private System.Windows.Forms.ComboBox serialDevices;
        private System.Windows.Forms.Button button2;
        private System.Windows.Forms.Label lbl_status_serial;
    }
}

