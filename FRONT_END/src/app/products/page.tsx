"use client";

import React from 'react';
import Image from 'next/image';
import { Chewy } from "next/font/google";

const chewyFont = Chewy({ subsets: ["latin"], weight: "400" });

const ProductPage = () => {
    const listing = {
        "product name": "Sample Product",
        location: "Sample Location",
        description: "This is a sample product description."
    };

    return (
        <div style={{ backgroundColor: 'rgb(245 244 227)' }}>
            <div style={{ backgroundColor: 'rgb(178 192 176)' }} className="h-14 flex justify-between items-center">
                <a href="/" className="w-14 px-2">
                    <Image src="/New_Hacks-removebg-preview.png" alt="Logo" width={56} height={56} />
                </a>
                <input type="search" name="query" placeholder="Search" className="border flex-1 h-10 rounded mx-20 px-2" />
                <div className="w-12 pr-2">
                    <svg style={{ fill: '#565656' }} xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512">
                        <path d="M406.5 399.6C387.4 352.9 341.5 320 288 320l-64 0c-53.5 0-99.4 32.9-118.5 79.6C69.9 362.2 48 311.7 48 256C48 141.1 141.1 48 256 48s208 93.1 208 208c0 55.7-21.9 106.2-57.5 143.6zm-40.1 32.7C334.4 452.4 296.6 464 256 464s-78.4-11.6-110.5-31.7c7.3-36.7 39.7-64.3 78.5-64.3l64 0c38.8 0 71.2 27.6 78.5 64.3zM256 512A256 256 0 1 0 256 0a256 256 0 1 0 0 512zm0-272a40 40 0 1 1 0-80 40 40 0 1 1 0 80zm-88-40a88 88 0 1 0 176 0 88 88 0 1 0 -176 0z" />
                    </svg>
                </div>
            </div>
            <div style={{ backgroundColor: 'rgb(245 244 227)' }} className="flex pt-10 my-auto">
                <div className="flex-1">
                    <Image style={{ width: '80%', borderRadius: '15px' }} className="mx-auto shadow-md hover:shadow-inner" src="/static/images/labour.jpg" alt="Product" width={500} height={500} />
                </div>
                <div className="flex-1 flex flex-col relative">
                    <div style={{ fontFamily: 'Chewy' }} className="text-6xl mb-px">{listing["product name"]}</div>
                    <div className="mb-10 underline">{listing.location}</div>
                    <div className="pr-5 leading-loose text-lg">{listing.description}</div>
                    <a href="mailto:abc@gmail.com" className="absolute mt-10 underline bottom-10 z-10">Connect!</a>
                </div>
            </div>
        </div>
    );
};

export default ProductPage;