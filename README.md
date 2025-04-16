<!-- Improved compatibility of back to top link: See: https://github.com/othneildrew/Best-README-Template/pull/73 -->
<a id="readme-top"></a>
<!--
*** Thanks for checking out the Best-README-Template. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Don't forget to give the project a star!
*** Thanks again! Now go create something AMAZING! :D
-->

<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->
[![Contributors][contributors-shield]][contributors-url]
[![Version][version-shield]][version-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![project_license][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]

<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/ggattoni/fake-book-index">
    <img src="https://cdn-icons-png.flaticon.com/512/2108/2108423.png" alt="Logo" width="160" height="160">
  </a>

<h3 align="center">Fake Book Index</h3>

  <p align="center">
    Telegram bot that given the name of a jazz standard retrieves the books where the lead sheet can be found.
    <br />
    <a href="https://github.com/ggattoni/fake-book-index"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <!-- <a href="https://github.com/ggattoni/fake-book-index">View Demo</a>
    &middot; -->
    <a href="https://github.com/ggattoni/fake-book-index/issues/new?labels=bug&template=bug-report---.md">Report Bug</a>
    &middot;
    <a href="https://github.com/ggattoni/fake-book-index/issues/new?labels=enhancement&template=feature-request---.md">Request Feature</a>
  </p>
</div>

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>


## Built With

* [![Python][Python]][Python-url]
* [![Ruff][Ruff]][Ruff-url]

<!-- <p align="right">(<a href="#readme-top">back to top</a>)</p> -->

<!-- GETTING STARTED -->
## Getting Started

To get a local copy up and running follow these simple example steps.

### Prerequisites

* Install docker by following the instructions on [docker's docs](https://docs.docker.com/)

### Installation

1. Pull the latest image
   ```sh
   docker pull ghcr.io/ggattoni/fake-book-index:latest
   ```
2. Run the container
   ```sh
   docker run --env BOT_TOKEN=123456:ABC-DEF1234ghIkl-zyx57W2v1u123ew11 -d fake-book-index
   ```

<!-- <p align="right">(<a href="#readme-top">back to top</a>)</p> -->

<!-- USAGE EXAMPLES -->
## Usage

On your telegram bot use the command `\start` to start the bot, then simply send a message with the name of the desired song and the bot will tell you in which books you can find the lead sheet for the specified song.

<!-- _For more examples, please refer to the [Documentation](https://example.com)_ -->

<!-- <p align="right">(<a href="#readme-top">back to top</a>)</p> -->

<!-- ROADMAP -->
## Roadmap

- [x] Publish docker image
- [ ] Use multipage message as answer instead of multiple messages

See the [open issues](https://github.com/ggattoni/fake-book-index/issues) for a full list of proposed features (and known issues).

<!-- <p align="right">(<a href="#readme-top">back to top</a>)</p> -->

<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/amazing_feature`)
3. Commit your Changes (`git commit -m 'feat: add some amazing feature'`)
4. Push to the Branch (`git push origin feature/amazing_feature`)
5. Open a Pull Request

<!-- <p align="right">(<a href="#readme-top">back to top</a>)</p> -->

<!-- ### Top contributors:

<a href="https://github.com/ggattoni/fake-book-index/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=ggattoni/fake-book-index" alt="contrib.rocks image" />
</a> -->

<!-- LICENSE -->
## License

Distributed under the MIT license. See [`LICENSE.txt`](LICENSE.txt) for more information.

<!-- <p align="right">(<a href="#readme-top">back to top</a>)</p> -->

<!-- CONTACT -->
## Contact

Giacomo Gattoni - ggattoni3@gmail.com

<!-- Project Link: [https://github.com/ggattoni/fake-book-index](https://github.com/ggattoni/fake-book-index) -->

<!-- <p align="right">(<a href="#readme-top">back to top</a>)</p> -->

<!-- ACKNOWLEDGMENTS -->
<!-- ## Acknowledgments -->


<!-- <p align="right">(<a href="#readme-top">back to top</a>)</p> -->

<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/ggattoni/fake-book-index.svg?style=for-the-badge
[contributors-url]: https://github.com/ggattoni/fake-book-index/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/ggattoni/fake-book-index.svg?style=for-the-badge
[forks-url]: https://github.com/ggattoni/fake-book-index/network/members
[version-shield]: https://img.shields.io/github/v/tag/ggattoni/fake-book-index?style=for-the-badge
[version-url]: https://github.com/ggattoni/fake-book-index/tags
[stars-shield]: https://img.shields.io/github/stars/ggattoni/fake-book-index.svg?style=for-the-badge
[stars-url]: https://github.com/ggattoni/fake-book-index/stargazers
[issues-shield]: https://img.shields.io/github/issues/ggattoni/fake-book-index.svg?style=for-the-badge
[issues-url]: https://github.com/ggattoni/fake-book-index/issues
[license-shield]: https://img.shields.io/github/license/ggattoni/fake-book-index.svg?style=for-the-badge
[license-url]: https://github.com/ggattoni/fake-book-index/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/giacomo-gattoni
[product-screenshot]: assets/images/xtechai.png
[Python]: https://img.shields.io/badge/python-3776AB?style=for-the-badge&logo=python&logoColor=white
[Python-url]: https://www.python.org/
[SymPy]: https://img.shields.io/badge/sympy-3B5526?style=for-the-badge&logo=sympy&logoColor=white
[SymPy-url]: https://www.sympy.org/
[Ruff]: https://img.shields.io/badge/ruff-D7FF64?style=for-the-badge&logo=ruff&logoColor=black
[Ruff-url]: https://docs.astral.sh/ruff/