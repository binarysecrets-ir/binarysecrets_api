import { useEffect, useRef, useState } from "react";
import { Link, useLocation } from "react-router-dom";

export default function Navbar() {
    const [open, setOpen] = useState(false);
    const dropdownRef = useRef(null);
    const location = useLocation();

    useEffect(() => {
        setOpen(false);
    }, [location.pathname]);

    useEffect(() => {
        const handleClickOutside = (event) => {
            if (
                dropdownRef.current &&
                !dropdownRef.current.contains(event.target)
            ) {
                setOpen(false);
            }
        };

        document.addEventListener("mousedown", handleClickOutside);

        return () => {
            document.removeEventListener("mousedown", handleClickOutside);
        };
    }, []);

    return (
        <header className="h-16 border-b border-gray-200 bg-white">
            <div className="mx-auto flex h-full max-w-7xl items-center px-6">

                {/* Logo */}
                <Link
                    to="/"
                    className="text-lg font-bold tracking-tight text-gray-900"
                >
                    Binary API
                </Link>

                {/* Navigation */}
                <nav className="ml-10 flex items-center gap-1">

                    <Link
                        to="/"
                        className="rounded-lg px-3 py-2 text-sm text-gray-600 transition hover:bg-gray-100 hover:text-gray-900 vazir"
                    >
                        خانه
                    </Link>

                    {/* Dropdown */}
                    <div
                        ref={dropdownRef}
                        className="relative"
                    >
                        <button
                            onClick={() => setOpen(!open)}
                            className={`flex h-10 items-center gap-1.5 rounded-lg px-3 text-sm transition ${
                                open
                                    ? "bg-gray-100 text-gray-900"
                                    : "text-gray-600 hover:bg-gray-100 hover:text-gray-900"
                            }`}
                        >
                            APIs

                            <svg
                                className={`h-3.5 w-3.5 transition-transform duration-200 ${
                                    open ? "rotate-180" : ""
                                }`}
                                viewBox="0 0 24 24"
                                fill="none"
                                stroke="currentColor"
                                strokeWidth="2"
                            >
                                <path d="m6 9 6 6 6-6" />
                            </svg>
                        </button>

                        {/* Menu */}
                        {open && (
                            <div className="absolute left-0 top-[calc(100%+8px)] z-50 w-72 rounded-xl border border-gray-200 bg-white p-1.5 shadow-xl shadow-black/5">

                                <Link
                                    to="/apis"
                                    className="flex gap-3 rounded-lg p-2.5 transition hover:bg-gray-50"
                                >
                                    <div className="flex h-9 w-9 shrink-0 items-center justify-center rounded-lg border border-gray-200 bg-gray-50 text-[10px] font-bold text-gray-600">
                                        API
                                    </div>

                                    <div>
                                        <div className="text-sm font-semibold text-gray-900">
                                            همه APIها
                                        </div>

                                        <div className="mt-0.5 text-xs text-gray-500">
                                            Explore available APIs
                                        </div>
                                    </div>
                                </Link>

                                <Link
                                    to="/apis/image"
                                    className="flex gap-3 rounded-lg p-2.5 transition hover:bg-gray-50"
                                >
                                    <div className="flex h-9 w-9 shrink-0 items-center justify-center rounded-lg border border-gray-200 bg-gray-50 text-[10px] font-bold text-gray-600">
                                        IMG
                                    </div>

                                    <div>
                                        <div className="text-sm font-semibold text-gray-900">
                                            Image API
                                        </div>

                                        <div className="mt-0.5 text-xs text-gray-500">
                                            Compress and process images
                                        </div>
                                    </div>
                                </Link>

                                <Link
                                    to="/apis/pdf"
                                    className="flex gap-3 rounded-lg p-2.5 transition hover:bg-gray-50"
                                >
                                    <div className="flex h-9 w-9 shrink-0 items-center justify-center rounded-lg border border-gray-200 bg-gray-50 text-[10px] font-bold text-gray-600">
                                        PDF
                                    </div>

                                    <div>
                                        <div className="text-sm font-semibold text-gray-900">
                                            PDF API
                                        </div>

                                        <div className="mt-0.5 text-xs text-gray-500">
                                            Process PDF documents
                                        </div>
                                    </div>
                                </Link>

                            </div>
                        )}
                    </div>

                    <Link
                        to="/docs"
                        className="rounded-lg px-3 py-2 text-sm text-gray-600 transition hover:bg-gray-100 hover:text-gray-900"
                    >
                        راهنما
                    </Link>

                </nav>

                {/* Actions */}
                <div className="ml-auto flex items-center gap-2">

                    <Link
                        to="/login"
                        className="rounded-lg px-3.5 py-2 text-sm font-medium text-gray-600 transition hover:bg-gray-100 hover:text-gray-900 vazir"
                    >
                        ورود
                    </Link>

                    <Link
                        to="/signup"
                        className="rounded-lg bg-gray-900 px-4 py-2 text-sm font-medium text-white transition hover:bg-gray-800 vazir"
                    >
                        ثبت نام
                    </Link>

                </div>
            </div>
        </header>
    );
}