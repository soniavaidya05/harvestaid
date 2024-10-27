"use client";

import React, { useState } from 'react';
import { Chewy } from "next/font/google";


const chewyFont = Chewy({ subsets: ["latin"], weight: "400" });

const LoginPage: React.FC = () => {
    const [email, setEmail] = useState('');
    const [password, setPassword] = useState('');

    const handleLogin = (event: React.FormEvent) => {
        event.preventDefault();
        // Handle login logic here
        console.log('Email:', email);
        console.log('Password:', password);
    };

    return (
        <div
            style={{ backgroundColor: "rgb(245, 244, 227)" }}
            className="flex h-screen flex-col justify-center items-center"
        >
            <div className="bg-[#b2c0b0] p-8 rounded-lg drop-shadow-md">
                <h2 className={`text-3xl mb-6 text-center ${chewyFont.className}`}>Login</h2>
                <form onSubmit={handleLogin} className="flex flex-col">
                    <div className="mb-4">
                        <label htmlFor="email" className="block text-lg mb-2">Email:</label>
                        <input
                            type="email"
                            id="email"
                            value={email}
                            onChange={(e) => setEmail(e.target.value)}
                            required
                            className="w-full px-3 py-2 border rounded"
                        />
                    </div>
                    <div className="mb-6">
                        <label htmlFor="password" className="block text-lg mb-2">Password:</label>
                        <input
                            type="password"
                            id="password"
                            value={password}
                            onChange={(e) => setPassword(e.target.value)}
                            required
                            className="w-full px-3 py-2 border rounded"
                        />
                    </div>
                    <button
                        type="submit"
                        className={`px-5 py-2 text-xl text-white bg-[#b2c0b0] border-b-4 border-[#8b9c8d] rounded transition ease-in-out transform hover:translate-y-1 hover:border-0 ${chewyFont.className}`}
                    >
                        Login
                    </button>
                </form>
            </div>
        </div>
    );
};

export default LoginPage;