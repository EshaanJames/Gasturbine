import streamlit as st
from PIL import Image
def app(df):
    st.markdown(
        """<p style='color:red'>A gas turbine is a rotary machine in which the chemical energy of the fuel is converted into mechanical energy or kinetic energy in terms of shaft power. 
        In other words, it is a mechanical power or thrust delivering machine. It uses a gaseous working fluid for this purpose. The generated mechanical power can be used by industrial devices.
         There is a continuous flow of the working fluid in a gas turbine. Power generation gas turbines are the ones that produce shaft power. To propel an aircraft, gas turbines are used that 
         convert fuel energy into kinetic energy for the generation of thrust. Fig. 1 below shows a typical representation of Gas turbine. """,
        unsafe_allow_html=True)
    img1 = Image.open("Turbine.png")
    st.image(img1,caption='Gas Turbine')

    with st.expander('View Database'):
        st.dataframe(df)
    st.subheader('Columns description')
    col_name, col_dtype, col_display = st.columns(3)
    if col_name.checkbox('Show all column names'):
        st.table(df.columns)
    if col_dtype.checkbox('View column datatype'):
        st.write(list(df.dtypes))

    with st.expander('Application of Gas Turbine'):
        st.write("""
        Major applications of gas turbines are found in:
        
        * As the direct and mechanical drive for various industries
        * Aviation
        * Electrical Power generation
        * Oil and gas industry
        * Marine propulsion
        * Turbo generators
        * Turbo-compressor
        * Automotive sector""")

    with st.expander('Working principle of gas turbine'):
        st.markdown("""<p style = 'color:grey'>
        The working of a gas turbine is based on the thermodynamic Brayton Cycle. <br>
        The Brayton cycle consists of two adiabatic work transfers and two constant pressure heat transfer heat processes (Fig 2). <br>
        The gas undergoes an isentropic, adiabatic compression in State1 to State2. 
        This process increases the temperature, pressure, and density of the gas. <br>
        Next, heat is added at constant pressure in State 2 to State 3. For a gas turbine, a combustion process adds heat. <br>
        During State 3 to State 4, the gas passes through an adiabatic isentropic turbine that decreases the temperature and pressure of the gas. <br>
        In the case of a closed gas turbine Brayton cycle, heat is removed from the gas between State 4 and State 1 via a heat exchanger.<br>
        """, unsafe_allow_html=True)
        img2 = Image.open("Brayton cyxle.png")
        st.image(img2, caption ="Brayton Cycle")
    with st.expander('Operating Principle'):
        st.markdown("""<p style = 'color:pink'>
        Let’s understand the basic operating principle of a gas turbine with the following example:
        Imagine there is a rocket in which fuel is going to burn thereby creating high-pressure exhaust gas. 
        According to energy conservation law, in the high-pressure exhaust gas, the chemical energy of the fuel is converted into mechanical energy.
        The thrust of the exhaust gas tries to move the rocket forward when the rocket is fired. 
        Now the question is if one fixes the rocket body with a mechanical structure in order to prevent its movement. What will happen?""", unsafe_allow_html=True)

        st.markdown("""<p style = 'color:pink'>
        In such a case, the high-pressure exhaust gas releases but in the backward direction.
        Now another case is that what if we add a set of turbine blades to this back-fired exhaust gas?""", unsafe_allow_html=True)

        st.markdown("""<p style = 'color:pink'>
        The released mechanical energy which is in the linear backward direction will transform into rotational movement of the turbine shaft which is a big success. 
        This means the chemical energy of the fuel gas is transformed into rotational mechanical energy of the turbine shaft as shown in Fig. 3.
        """, unsafe_allow_html=True)
        img3 = Image.open("operating.png")

        st.image(img3, caption="Gas Turbine working principle")

        st.markdown("""<p style = 'color:pink'>
        In simple words, in a gas turbine, hot gases move through a multistage gas turbine.
        It has both stationary and moving blades just like a steam turbine.
        he stationary blades adjust their velocity and guide the moving gases to rotor blades. 
        The turbine’s shaft is coupled to a generator.
        """, unsafe_allow_html=True)

    with st.expander("Working principle of a gas turbine in a power plant"):

        st.markdown("""<p style = 'color:yellow'>
        In a gas turbine power plant, there is a generator known as an electrical machine and this generator needs a prime 
        mover which is a gas turbine in order to generate electricity """, unsafe_allow_html=True)
        img4 = Image.open("primemover.png")
        st.image(img4, caption = "Gas Turbine as a prime mover")

        st.markdown("""<p style = 'color:yellow'>
                It transforms the fuel’s chemical energy into mechanical energy or in other words converting natural gas into mechanical energy.
                The generated mechanical energy is then transferred to the generator’s shaft through a gearbox. 
                Now the turbine can create electrical energy """, unsafe_allow_html=True)
        img5 = Image.open("mech eng.png")
        st.image(img5, caption="Gas Turbine as a prime mover")

        st.markdown("""<p style = 'color:yellow>
        
        """,unsafe_allow_html=True )
        img6 = Image.open("transmission.png")
        st.image(img6, caption = " Transmission lines in power generation")
    with st.expander("Working of a gas turbine in oil and gas industry"):

        st.write("""
        Points to be noted:
        * For the oil and gas production process, the turbine is coupled to a compressor or a pump instead of coupling with a turbine.
        * An arrangement similar to a steam turbine is considered when one uses a gas turbine to drive a compressor.
        * The header tanks and lube oil are required in the auxiliary piping system.
        * The exhaust system should be considered which has ducting to few heat recovery systems, that is, a process heater or a steam raising plant.
        * There should be a provision for maintenance and operation to all machinery.
        * Outside the compressor house, combustion air must be taken to the turbine burner from a safe location. Most likely required items are inlet silencer and filter
        """)
    with st.expander("Components of gas tubine"):
        img7 = Image.open("comp.png")
        st.write("""
                * Air Compressor
                * Combustion Chamber
                * Tubine
                """)
        st.image(img7, caption="Bas turine components")

        st.subheader("1. Air Compressor")

        st.markdown("""<p style = 'color:orange'>
        With the combustion chamber between the air compressor and turbine, both the air compressor and turbine are mounted on either end on a common shaft. Gas turbines require a starting motor as they are not self-starting. The use of an air compressor is to suck the air and compress it thereby increasing its pressure. Axial design type compressors (multi-stage) are preferred for the most advanced and large gas turbines.
        """, unsafe_allow_html=True)
        img8 = Image.open("compressor.png")
        st.image(img8, caption="High-performance compressor assemblly")
        st.subheader("2. Combustion chamber")

        st.markdown("""<p style = 'color:skyblue'>
        Here the compressed air is combined with fuel where the resulting fuel-air mixture is burnt and delivers the combustion products to the gas turbine. With high pressure of air, the fuel mixture burns quite well. Nowadays liquid fuel, gaseous fuel, or natural gas is used in gas turbines. Generally, three types of combustion chambers are used:
                """, unsafe_allow_html=True)
        st.write("""
        * annular combustor chambers
        * can (multican chambers)
        * can-annular combustor chamber
        """)
        st.markdown("""<p style = 'color:skyblue'>
        Fuel is injected at the upstream end of the burner in the form of a highly atomized spray. Fuel nozzles may be a simplex type or dual fuel type. Some gas turbines are “bi-fuel” which means they have to ability to burn a mixture of gas and liquid fuel.
                """, unsafe_allow_html=True)
        img9 = Image.open("chamber.png")
        st.image(img9, caption="Combustion chamber of a gas turbine")
        st.subheader("3. Turbine")
        st.markdown("""<p style = 'color:lightblue'>
        There is a multistage gas turbine from where hot gases move and the kinetic energy is transformed into shaft horsepower. A gas turbine has both stationary and moving blades just like a steam turbine. The purpose of stationary blades is to guide the moving gases to the rotor blades and then adjust their velocity. The turbine’s shaft is coupled to a generator.
        """, unsafe_allow_html=True)

    with st.expander("Advantages of gas turbine"):
        st.write("""
        * Fuel storage requires less area and handling is easy.
        * The maintenance cost is less.
        * Construction is quite simple.
        * As compared to steam power plants, it does not require a condenser, boiler, and other accessories.
        * Fuels such as kerosene, benzene, paraffin, and powdered coal can be used which are cheaper than other petrol and diesel.
        * In the areas of water scarcity, gas turbines can be used.
        * It creates less pollution.
        * It requires less amount of water.""")
    with st.expander("Disadvantages of Gas turbine"):
        st.write("""
        * Most of the developed power is used to drive the compressor.
        * This is the reason that a gas turbine has low thermal efficiency.
        * High-frequency noise comes from the compressor which is again questionable.
        * For various parts of the turbine, special metals and alloys are used because the running speed of the turbine is 40000 to 100000 rpm and the operating temperature is 1100 to 1260 degrees Celsius.
        """)
    with st.expander("Watch this video for further information"):
        st.video("https://www.youtube.com/watch?v=GF-70yncAVY")



