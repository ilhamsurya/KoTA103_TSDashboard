"""Plotly Dash HTML layout override."""

timeseries_layout = """
<!DOCTYPE html>
    <html>
    <!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Time Series Dashboard App</title>
    <meta name="author" content="David Grzyb" />
    <meta name="description" content="" />

    <!-- Tailwind -->
    <link
      href="https://unpkg.com/tailwindcss/dist/tailwind.min.css"
      rel="stylesheet"
    />
    <style>
      @import url('https://fonts.googleapis.com/css?family=Karla:400,700&display=swap');
      .font-family-karla {
        font-family: karla;
      }
      .bg-sidebar {
        background: #3d68ff;
      }
      .cta-btn {
        color: #3d68ff;
      }
      .upgrade-btn {
        background: #1947ee;
      }
      .upgrade-btn:hover {
        background: #0038fd;
      }
      .active-nav-link {
        background: #1947ee;
      }
      .nav-item:hover {
        background: #1947ee;
      }
      .account-link:hover {
        background: #3d68ff;
      }
    </style>
             {%metas%}
            <title>{%title%}</title>
            {%favicon%}
            {%css%}
  </head>
  <body class="bg-gray-100 font-family-karla flex">

    <aside class="relative bg-sidebar h-screen w-64 hidden sm:block shadow-xl">
      <div class="p-6">
        <a
          href="/"
          class="text-white text-3xl font-semibold uppercase hover:text-gray-300"
          >Time Series Dashboard</a
        >
        <button
          class="w-full bg-white cta-btn font-semibold py-2 mt-5 rounded-br-lg rounded-bl-lg rounded-tr-lg shadow-lg hover:shadow-xl hover:bg-gray-300 flex items-center justify-center"
        >
          <i class="fab fa-empire mr-3"></i> Pelanggaran Laut
        </button>
      </div>

      <nav class="text-white text-base font-semibold pt-3">
        <a
          href="/dashboard"
          class="flex items-center active-nav-link text-white py-4 pl-6 nav-item"
        >
          <i class="far fa-clock mr-3"></i>
          Time Series Analysis
        </a>
        <a
          href="/forecasting"
          class="flex items-center text-white opacity-75 hover:opacity-100 py-4 pl-6 nav-item"
        >
          <i class="fas fa-eye mr-3"></i>
          Forecasting
        </a>
        <a
          href="/map"
          class="flex items-center text-white opacity-75 hover:opacity-100 py-4 pl-6 nav-item"
        >
          <i class="fas fa-globe-asia mr-3"></i>
          Map Pelanggaran
        </a>
      </nav>
      <a
        href="#"
        class="absolute w-full upgrade-btn bottom-0 active-nav-link text-white flex items-center justify-center py-4"
      >
        <i class="fas fa-question-circle mr-3"></i>
        KoTA103 18
      </a>
    </aside>

    <div class="w-full flex flex-col h-screen overflow-y-hidden">
      <!-- Desktop Header -->
      <header class="w-full items-center bg-white py-2 px-6 hidden sm:flex">
        <div class="w-1/2"></div>
        <div x-data="{ isOpen: false }" class="relative w-1/2 flex justify-end">
          <button
            @click="isOpen = !isOpen"
            class="realtive z-10 w-12 h-12 rounded-full overflow-hidden border-4 border-gray-400 hover:border-gray-300 focus:border-gray-300 focus:outline-none"
          >
            <img
              src="https://images.unsplash.com/photo-1596854273338-cbf078ec7071?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=400&q=400"
            />
          </button>
          <button
            x-show="isOpen"
            @click="isOpen = false"
            class="h-full w-full fixed inset-0 cursor-default"
          ></button>
          <div
            x-show="isOpen"
            class="absolute w-32 bg-white rounded-lg shadow-lg py-2 mt-16"
          >
            <a href="#" class="block px-4 py-2 account-link hover:text-white"
              >Account</a
            >
            <a href="#" class="block px-4 py-2 account-link hover:text-white"
              >Support</a
            >
            <a href="#" class="block px-4 py-2 account-link hover:text-white"
              >Sign Out</a
            >
          </div>
        </div>
      </header>

      <!-- Mobile Header & Nav -->
      <header
        x-data="{ isOpen: false }"
        class="w-full bg-sidebar py-5 px-6 sm:hidden"
      >
        <div class="flex items-center justify-between">
          <a
            href="index.html"
            class="text-white text-3xl font-semibold uppercase hover:text-gray-300"
            >Time Series Dashboard</a
          >
          <button
            @click="isOpen = !isOpen"
            class="text-white text-3xl focus:outline-none"
          >
            <i x-show="!isOpen" class="fas fa-bars"></i>
            <i x-show="isOpen" class="fas fa-times"></i>
          </button>
        </div>

        <!-- Dropdown Nav -->
        <nav :class="isOpen ? 'flex': 'hidden'" class="flex flex-col pt-4">
          <a
            href="index.html"
            class="flex items-center active-nav-link text-white py-2 pl-4 nav-item"
          >
            <i class="fas fa-clock mr-3"></i>
            Time Series Analysis
          </a>
          <a
            href="blank.html"
            class="flex items-center text-white opacity-75 hover:opacity-100 py-2 pl-4 nav-item"
          >
            <i class="fas fa-eye mr-3"></i>
            Forecasting
          </a>
          <a
            href="tables.html"
            class="flex items-center text-white opacity-75 hover:opacity-100 py-2 pl-4 nav-item"
          >
            <i class="fas fa-globe-asia mr-3"></i>
            Map Pelanggaran
          </a>
          <a
            href="#"
            class="flex items-center text-white opacity-75 hover:opacity-100 py-2 pl-4 nav-item"
          >
            <i class="fas fa-user mr-3"></i>
            My Account
          </a>
          <a
            href="#"
            class="flex items-center text-white opacity-75 hover:opacity-100 py-2 pl-4 nav-item"
          >
            <i class="fas fa-sign-out-alt mr-3"></i>
            Sign Out
          </a>
          <button
            class="w-full bg-white cta-btn font-semibold py-2 mt-3 rounded-lg shadow-lg hover:shadow-xl hover:bg-gray-300 flex items-center justify-center"
          >
            <i class="fas fa-question-circle mr-3"></i> KoTA103 18
          </button>
        </nav>
        <!-- <button class="w-full bg-white cta-btn font-semibold py-2 mt-5 rounded-br-lg rounded-bl-lg rounded-tr-lg shadow-lg hover:shadow-xl hover:bg-gray-300 flex items-center justify-center">
                <i class="fas fa-plus mr-3"></i> New Report
            </button> -->
      </header>


      <div class="w-full overflow-x-hidden border-t flex flex-col">
        <main class="w-full flex-grow p-6">
          <h1 class="text-3xl text-black pb-6">Time Series Analysis</h1>
               {%app_entry%}
            </div>
          </div>
        </main>


      </div>
    </div>

    <!-- AlpineJS -->
    <script
      src="https://cdn.jsdelivr.net/gh/alpinejs/alpine@v2.x.x/dist/alpine.min.js"
      defer
    ></script>
    <!-- Font Awesome -->
    <script
      src="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.13.0/js/all.min.js"
      integrity="sha256-KzZiKy0DWYsnwMF+X1DvQngQ2/FxF7MF3Ff72XcpuPs="
      crossorigin="anonymous"
    ></script>
    <!-- ChartJS -->
    <script
      src="https://cdnjs.cloudflare.com/ajax/libs/Chart.js/2.9.3/Chart.min.js"
      integrity="sha256-R4pqcOYV8lt7snxMQO/HSbVCFRPMdrhAFMH+vr9giYI="
      crossorigin="anonymous"
    ></script>

  </body>
         <footer>
                {%config%}
                {%scripts%}
                {%renderer%}
            </footer>
</html>

       
"""

forecasting_layout = """
<!DOCTYPE html>
    <html>
    <!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Time Series Dashboard App</title>
    <meta name="author" content="David Grzyb" />
    <meta name="description" content="" />

    <!-- Tailwind -->
    <link
      href="https://unpkg.com/tailwindcss/dist/tailwind.min.css"
      rel="stylesheet"
    />
    <style>
      @import url('https://fonts.googleapis.com/css?family=Karla:400,700&display=swap');
      .font-family-karla {
        font-family: karla;
      }
      .bg-sidebar {
        background: #3d68ff;
      }
      .cta-btn {
        color: #3d68ff;
      }
      .upgrade-btn {
        background: #1947ee;
      }
      .upgrade-btn:hover {
        background: #0038fd;
      }
      .active-nav-link {
        background: #1947ee;
      }
      .nav-item:hover {
        background: #1947ee;
      }
      .account-link:hover {
        background: #3d68ff;
      }
    </style>
             {%metas%}
            <title>{%title%}</title>
            {%favicon%}
            {%css%}
  </head>
  <body class="bg-gray-100 font-family-karla flex">

    <aside class="relative bg-sidebar h-screen w-64 hidden sm:block shadow-xl">
      <div class="p-6">
        <a
          href="/"
          class="text-white text-3xl font-semibold uppercase hover:text-gray-300"
          >Time Series Dashboard</a
        >
        <button
          class="w-full bg-white cta-btn font-semibold py-2 mt-5 rounded-br-lg rounded-bl-lg rounded-tr-lg shadow-lg hover:shadow-xl hover:bg-gray-300 flex items-center justify-center"
        >
          <i class="fab fa-empire mr-3"></i> Pelanggaran Laut
        </button>
      </div>

      <nav class="text-white text-base font-semibold pt-3">
        <a
          href="/timeseries"
          class="flex items-center  text-white py-4 pl-6 nav-item"
        >
          <i class="far fa-clock mr-3"></i>
          Time Series Analysis
        </a>
        <a
          href="/forecasting"
          class="flex items-center active-nav-link text-white opacity-75 hover:opacity-100 py-4 pl-6 nav-item"
        >
          <i class="fas fa-eye mr-3"></i>
          Forecasting
        </a>
        <a
          href="/map"
          class="flex items-center text-white opacity-75 hover:opacity-100 py-4 pl-6 nav-item"
        >
          <i class="fas fa-globe-asia mr-3"></i>
          Map Pelanggaran
        </a>
      </nav>
      <a
        href="#"
        class="absolute w-full upgrade-btn bottom-0 active-nav-link text-white flex items-center justify-center py-4"
      >
        <i class="fas fa-question-circle mr-3"></i>
        KoTA103 18
      </a>
    </aside>

    <div class="w-full flex flex-col h-screen overflow-y-hidden">
      <!-- Desktop Header -->
      <header class="w-full items-center bg-white py-2 px-6 hidden sm:flex">
        <div class="w-1/2"></div>
        <div x-data="{ isOpen: false }" class="relative w-1/2 flex justify-end">
          <button
            @click="isOpen = !isOpen"
            class="realtive z-10 w-12 h-12 rounded-full overflow-hidden border-4 border-gray-400 hover:border-gray-300 focus:border-gray-300 focus:outline-none"
          >
            <img
              src="https://images.unsplash.com/photo-1596854273338-cbf078ec7071?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=400&q=400"
            />
          </button>
          <button
            x-show="isOpen"
            @click="isOpen = false"
            class="h-full w-full fixed inset-0 cursor-default"
          ></button>
          <div
            x-show="isOpen"
            class="absolute w-32 bg-white rounded-lg shadow-lg py-2 mt-16"
          >
            <a href="#" class="block px-4 py-2 account-link hover:text-white"
              >Account</a
            >
            <a href="#" class="block px-4 py-2 account-link hover:text-white"
              >Support</a
            >
            <a href="#" class="block px-4 py-2 account-link hover:text-white"
              >Sign Out</a
            >
          </div>
        </div>
      </header>

      <!-- Mobile Header & Nav -->
      <header
        x-data="{ isOpen: false }"
        class="w-full bg-sidebar py-5 px-6 sm:hidden"
      >
        <div class="flex items-center justify-between">
          <a
            href="index.html"
            class="text-white text-3xl font-semibold uppercase hover:text-gray-300"
            >Time Series Dashboard</a
          >
          <button
            @click="isOpen = !isOpen"
            class="text-white text-3xl focus:outline-none"
          >
            <i x-show="!isOpen" class="fas fa-bars"></i>
            <i x-show="isOpen" class="fas fa-times"></i>
          </button>
        </div>

        <!-- Dropdown Nav -->
        <nav :class="isOpen ? 'flex': 'hidden'" class="flex flex-col pt-4">
          <a
            href="index.html"
            class="flex items-center active-nav-link text-white py-2 pl-4 nav-item"
          >
            <i class="fas fa-clock mr-3"></i>
            Time Series Analysis
          </a>
          <a
            href="blank.html"
            class="flex items-center text-white opacity-75 hover:opacity-100 py-2 pl-4 nav-item"
          >
            <i class="fas fa-eye mr-3"></i>
            Forecasting
          </a>
          <a
            href="tables.html"
            class="flex items-center text-white opacity-75 hover:opacity-100 py-2 pl-4 nav-item"
          >
            <i class="fas fa-globe-asia mr-3"></i>
            Map Pelanggaran
          </a>
          <a
            href="#"
            class="flex items-center text-white opacity-75 hover:opacity-100 py-2 pl-4 nav-item"
          >
            <i class="fas fa-user mr-3"></i>
            My Account
          </a>
          <a
            href="#"
            class="flex items-center text-white opacity-75 hover:opacity-100 py-2 pl-4 nav-item"
          >
            <i class="fas fa-sign-out-alt mr-3"></i>
            Sign Out
          </a>
          <button
            class="w-full bg-white cta-btn font-semibold py-2 mt-3 rounded-lg shadow-lg hover:shadow-xl hover:bg-gray-300 flex items-center justify-center"
          >
            <i class="fas fa-question-circle mr-3"></i> KoTA103 18
          </button>
        </nav>
        <!-- <button class="w-full bg-white cta-btn font-semibold py-2 mt-5 rounded-br-lg rounded-bl-lg rounded-tr-lg shadow-lg hover:shadow-xl hover:bg-gray-300 flex items-center justify-center">
                <i class="fas fa-plus mr-3"></i> New Report
            </button> -->
      </header>


      <div class="w-full overflow-x-hidden border-t flex flex-col">
        <main class="w-full flex-grow p-6">
          <h1 class="text-3xl text-black pb-6">Time Series Analysis</h1>
               {%app_entry%}
            </div>
          </div>
        </main>


      </div>
    </div>

    <!-- AlpineJS -->
    <script
      src="https://cdn.jsdelivr.net/gh/alpinejs/alpine@v2.x.x/dist/alpine.min.js"
      defer
    ></script>
    <!-- Font Awesome -->
    <script
      src="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.13.0/js/all.min.js"
      integrity="sha256-KzZiKy0DWYsnwMF+X1DvQngQ2/FxF7MF3Ff72XcpuPs="
      crossorigin="anonymous"
    ></script>
    <!-- ChartJS -->
    <script
      src="https://cdnjs.cloudflare.com/ajax/libs/Chart.js/2.9.3/Chart.min.js"
      integrity="sha256-R4pqcOYV8lt7snxMQO/HSbVCFRPMdrhAFMH+vr9giYI="
      crossorigin="anonymous"
    ></script>

  </body>
         <footer>
                {%config%}
                {%scripts%}
                {%renderer%}
            </footer>
</html>

       
"""

mapbox_layout = """
<!DOCTYPE html>
    <html>
    <!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Time Series Dashboard App</title>
    <meta name="author" content="David Grzyb" />
    <meta name="description" content="" />

    <!-- Tailwind -->
    <link
      href="https://unpkg.com/tailwindcss/dist/tailwind.min.css"
      rel="stylesheet"
    />
    <style>
      @import url('https://fonts.googleapis.com/css?family=Karla:400,700&display=swap');
      .font-family-karla {
        font-family: karla;
      }
      .bg-sidebar {
        background: #3d68ff;
      }
      .cta-btn {
        color: #3d68ff;
      }
      .upgrade-btn {
        background: #1947ee;
      }
      .upgrade-btn:hover {
        background: #0038fd;
      }
      .active-nav-link {
        background: #1947ee;
      }
      .nav-item:hover {
        background: #1947ee;
      }
      .account-link:hover {
        background: #3d68ff;
      }
    </style>
             {%metas%}
            <title>{%title%}</title>
            {%favicon%}
            {%css%}
  </head>
  <body class="bg-gray-100 font-family-karla flex">

    <aside class="relative bg-sidebar h-screen w-64 hidden sm:block shadow-xl">
      <div class="p-6">
        <a
          href="/"
          class="text-white text-3xl font-semibold uppercase hover:text-gray-300"
          >Time Series Dashboard</a
        >
        <button
          class="w-full bg-white cta-btn font-semibold py-2 mt-5 rounded-br-lg rounded-bl-lg rounded-tr-lg shadow-lg hover:shadow-xl hover:bg-gray-300 flex items-center justify-center"
        >
          <i class="fab fa-empire mr-3"></i> Pelanggaran Laut
        </button>
      </div>

      <nav class="text-white text-base font-semibold pt-3">
        <a
          href="/timeseries"
          class="flex items-center  text-white py-4 pl-6 nav-item"
        >
          <i class="far fa-clock mr-3"></i>
          Time Series Analysis
        </a>
        <a
          href="/forecasting"
          class="flex items-center  text-white opacity-75 hover:opacity-100 py-4 pl-6 nav-item"
        >
          <i class="fas fa-eye mr-3"></i>
          Forecasting
        </a>
        <a
          href="/map"
          class="flex items-center active-nav-link text-white opacity-75 hover:opacity-100 py-4 pl-6 nav-item"
        >
          <i class="fas fa-globe-asia mr-3"></i>
          Map Pelanggaran
        </a>
      </nav>
      <a
        href="#"
        class="absolute w-full upgrade-btn bottom-0 active-nav-link text-white flex items-center justify-center py-4"
      >
        <i class="fas fa-question-circle mr-3"></i>
        KoTA103 18
      </a>
    </aside>

    <div class="w-full flex flex-col h-screen overflow-y-hidden">
      <!-- Desktop Header -->
      <header class="w-full items-center bg-white py-2 px-6 hidden sm:flex">
        <div class="w-1/2"></div>
        <div x-data="{ isOpen: false }" class="relative w-1/2 flex justify-end">
          <button
            @click="isOpen = !isOpen"
            class="realtive z-10 w-12 h-12 rounded-full overflow-hidden border-4 border-gray-400 hover:border-gray-300 focus:border-gray-300 focus:outline-none"
          >
            <img
              src="https://images.unsplash.com/photo-1596854273338-cbf078ec7071?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=400&q=400"
            />
          </button>
          <button
            x-show="isOpen"
            @click="isOpen = false"
            class="h-full w-full fixed inset-0 cursor-default"
          ></button>
          <div
            x-show="isOpen"
            class="absolute w-32 bg-white rounded-lg shadow-lg py-2 mt-16"
          >
            <a href="#" class="block px-4 py-2 account-link hover:text-white"
              >Account</a
            >
            <a href="#" class="block px-4 py-2 account-link hover:text-white"
              >Support</a
            >
            <a href="#" class="block px-4 py-2 account-link hover:text-white"
              >Sign Out</a
            >
          </div>
        </div>
      </header>

      <!-- Mobile Header & Nav -->
      <header
        x-data="{ isOpen: false }"
        class="w-full bg-sidebar py-5 px-6 sm:hidden"
      >
        <div class="flex items-center justify-between">
          <a
            href="index.html"
            class="text-white text-3xl font-semibold uppercase hover:text-gray-300"
            >Time Series Dashboard</a
          >
          <button
            @click="isOpen = !isOpen"
            class="text-white text-3xl focus:outline-none"
          >
            <i x-show="!isOpen" class="fas fa-bars"></i>
            <i x-show="isOpen" class="fas fa-times"></i>
          </button>
        </div>

        <!-- Dropdown Nav -->
        <nav :class="isOpen ? 'flex': 'hidden'" class="flex flex-col pt-4">
          <a
            href="index.html"
            class="flex items-center active-nav-link text-white py-2 pl-4 nav-item"
          >
            <i class="fas fa-clock mr-3"></i>
            Time Series Analysis
          </a>
          <a
            href="blank.html"
            class="flex items-center text-white opacity-75 hover:opacity-100 py-2 pl-4 nav-item"
          >
            <i class="fas fa-eye mr-3"></i>
            Forecasting
          </a>
          <a
            href="tables.html"
            class="flex items-center text-white opacity-75 hover:opacity-100 py-2 pl-4 nav-item"
          >
            <i class="fas fa-globe-asia mr-3"></i>
            Map Pelanggaran
          </a>
          <a
            href="#"
            class="flex items-center text-white opacity-75 hover:opacity-100 py-2 pl-4 nav-item"
          >
            <i class="fas fa-user mr-3"></i>
            My Account
          </a>
          <a
            href="#"
            class="flex items-center text-white opacity-75 hover:opacity-100 py-2 pl-4 nav-item"
          >
            <i class="fas fa-sign-out-alt mr-3"></i>
            Sign Out
          </a>
          <button
            class="w-full bg-white cta-btn font-semibold py-2 mt-3 rounded-lg shadow-lg hover:shadow-xl hover:bg-gray-300 flex items-center justify-center"
          >
            <i class="fas fa-question-circle mr-3"></i> KoTA103 18
          </button>
        </nav>
        <!-- <button class="w-full bg-white cta-btn font-semibold py-2 mt-5 rounded-br-lg rounded-bl-lg rounded-tr-lg shadow-lg hover:shadow-xl hover:bg-gray-300 flex items-center justify-center">
                <i class="fas fa-plus mr-3"></i> New Report
            </button> -->
      </header>


      <div class="w-full overflow-x-hidden border-t flex flex-col">
        <main class="w-full flex-grow p-6">
          <h1 class="text-3xl text-black pb-6">Time Series Analysis</h1>
               {%app_entry%}
            </div>
          </div>
        </main>


      </div>
    </div>

    <!-- AlpineJS -->
    <script
      src="https://cdn.jsdelivr.net/gh/alpinejs/alpine@v2.x.x/dist/alpine.min.js"
      defer
    ></script>
    <!-- Font Awesome -->
    <script
      src="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.13.0/js/all.min.js"
      integrity="sha256-KzZiKy0DWYsnwMF+X1DvQngQ2/FxF7MF3Ff72XcpuPs="
      crossorigin="anonymous"
    ></script>
    <!-- ChartJS -->
    <script
      src="https://cdnjs.cloudflare.com/ajax/libs/Chart.js/2.9.3/Chart.min.js"
      integrity="sha256-R4pqcOYV8lt7snxMQO/HSbVCFRPMdrhAFMH+vr9giYI="
      crossorigin="anonymous"
    ></script>

  </body>
         <footer>
                {%config%}
                {%scripts%}
                {%renderer%}
            </footer>
</html>

       
"""
